import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()

EMAIL_HOST = os.getenv("EMAIL_HOST", "smtp.gmail.com")
EMAIL_PORT = int(os.getenv("EMAIL_PORT", "587"))
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
DRY_RUN = os.getenv("DRY_RUN", "False").lower() in ("true", "1")
TEST_EMAIL = os.getenv("TEST_EMAIL")

def send_email(to_address, subject, body):
    if DRY_RUN:
        print(f"🚀 [DRY RUN] Would send to {to_address} - Subject: {subject}")
        print(f"Body preview: {body[:80]}{'...' if len(body)>80 else ''}")
        return

    if TEST_EMAIL:
        print(f"🔧 [TEST MODE] Redirecting email to {TEST_EMAIL} instead of {to_address}")
        to_address = TEST_EMAIL

    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_USER
        msg['To'] = to_address
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
            server.starttls()
            server.login(EMAIL_USER, EMAIL_PASSWORD)
            server.send_message(msg)

        print(f"✅ Email sent to {to_address}")
    except Exception as e:
        print(f"❌ Failed to send email to {to_address}: {e}")


def send_summary_email(subject, body):
    summary_recipient = os.getenv("TEST_EMAIL") or EMAIL_USER
    print(f"📬 Sending summary report to {summary_recipient}")

    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_USER
        msg['To'] = summary_recipient
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
            server.starttls()
            server.login(EMAIL_USER, EMAIL_PASSWORD)
            server.send_message(msg)

        print(f"✅ Summary report emailed to {summary_recipient}")
    except Exception as e:
        print(f"❌ Failed to send summary email: {e}")
