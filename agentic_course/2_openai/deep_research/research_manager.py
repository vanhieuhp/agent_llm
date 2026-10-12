import asyncio

from agents import Runner, trace, gen_trace_id

from email_agent import email_agent
from planner_agent import planner_agent, WebSearchItem, WebSearchPlan
from search_agent import search_agent
from writer_agent import writer_agent, ReportData


class ResearchManager:
    async def run(self, query: str):
        """ Run the deep research process for a given query"""
        trace_id = gen_trace_id()
        with trace("Research trace", trace_id=trace_id):
            yield f"Starting research. Trace; https://platform.openai.com/traces/trace?trace_id={trace_id}"
            search_plan = await self.plan_searches(query)
            yield f"Searches planned, starting {len(search_plan.searches)} searches..."
            search_results = await self.perform_searches(search_plan)
            yield f"All searches complete, writing report..."
            report = await self.write_report(query, search_results)
            yield f"Report complete, sending email..."
            await self.send_report_email(report)
            yield f"Email sent successfully"
            yield report.markdown_report

    async def plan_searches(self, query: str) -> WebSearchPlan:
        """ Plan the searches to perform for a given query"""
        result = await Runner.run(planner_agent, f"Query: {query}")
        return result.final_output

    async def perform_searches(self, search_plan: WebSearchPlan) -> list[str]:
        tasks = [self.search(item) for item in search_plan.searches]
        results = await asyncio.gather(*tasks)
        return results

    async def search(self, item: WebSearchItem) -> str | None:
        print(f"Searching for {item.query} because {item.reason}")
        result = await Runner.run(search_agent, item.query)
        return result.final_output

    async def write_report(self, query: str, search_results: list[str]):
        print(f"Thinking about report...")
        input_message = f"Original query: {query}\n\nResearch: {search_results}"
        result = await Runner.run(writer_agent, input_message)
        return result.final_output

    async def send_report_email(self, report: ReportData):
        print(f"Writing email...")
        result = await Runner.run(email_agent, report.markdown_report)
        print(f"Email sent successfully")
        return report
