from agents import Agent
from pydantic import BaseModel, Field

INSTRUCTIONS = f"""
You are a research assistant. Given a user query, come up with a set of web searches
to perform to best answer the query. Output 5 terms to query for.
"""

class WebSearchItem(BaseModel):
    reason: str = Field(description="The reason why this search result was included in the summary.")
    query: str = Field(description="The search query used to obtain this result.")

class WebSearchPlan(BaseModel):
    searches: list[WebSearchItem] = Field(description="A list of web searches to perform to best answer the query.")

planner_agent = Agent(name="Planner Agent", instructions=INSTRUCTIONS, model="gpt-5.4-mini", output_type=WebSearchPlan)