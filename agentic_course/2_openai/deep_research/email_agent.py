from agents import Agent, function_tool

from messeger import send_email


@function_tool
def send_email_tool(subject: str, text_body: str, html_body: str) -> str:
    """
    Send out an email with the given subject and body to all sales prospects

    :param subject:  the subject of the email
    :param text_body:  the body of the email
    :param html_body: html version of the body
    """

    send_email(subject, text_body, html_body)
    return "Email sent successfully."

INSTRUCTIONS = """
You are provided with a detailed report. use your tool to send an email, converting the report into a clean,
well presented HTML email with an appropriate subject line.
"""

email_agent = Agent(name="Email Agent", instructions=INSTRUCTIONS, tools=[send_email_tool], model="gpt-5.4-mini")