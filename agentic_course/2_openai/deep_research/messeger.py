import os
import asyncio
import smtplib
from email.message import EmailMessage

import requests
from aiohttp import payload
from dotenv import load_dotenv

load_dotenv(override=True)

MODEL_NAME = os.getenv("DEEPSEEK_MODEL")

EMAIL_SMTP_SERVER = os.getenv("EMAIL_SMTP_SERVER")
EMAIL_SMTP_PORT = os.getenv("EMAIL_SMTP_PORT")
EMAIL_USERNAME = os.getenv("EMAIL_USERNAME")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_RECIPIENT = os.getenv("EMAIL_RECIPIENT")
EMAIL_SENDER = os.getenv("EMAIL_SENDER")

PUSHOVER_USER = os.getenv("PUSHOVER_USER")
PUSHOVER_TOKEN = os.getenv("PUSHOVER_TOKEN")
PUSHOVER_URL = os.getenv("PUSHOVER_URL")


def send_email(subject, text_body, html_body):
    msg = EmailMessage()
    msg["from"] = EMAIL_SENDER
    msg["to"] = EMAIL_RECIPIENT
    msg["subject"] = subject
    msg.set_content(text_body)
    msg.add_alternative(html_body, subtype="html")

    with smtplib.SMTP(EMAIL_SMTP_SERVER, EMAIL_SMTP_PORT) as smtp:
        smtp.starttls()
        smtp.login(EMAIL_USERNAME, EMAIL_PASSWORD)
        smtp.send_message(msg)

def push(message):
    print(f"Pushing message to Pushover: {message}")
    payload = {"token": PUSHOVER_TOKEN, "user": PUSHOVER_USER, "message": message}
    requests.post(PUSHOVER_URL, data=payload)
