from datetime import datetime, timedelta
import get_lastest_records as lc
import send_email_alert as se
from dotenv import load_dotenv
import os

def should_send_email(record):
    created_time_str = record.get("Created_Time")
    created_time = datetime.fromisoformat(created_time_str[:-6])  # Remove timezone offset from the string

    now = datetime.utcnow()
    days_difference = (now - created_time).days

    if created_time.weekday() in (0, 1, 2, 3):  # Tuesday, Wednesday, Thursday, Friday
        if days_difference == 1:
            return True
    elif created_time.weekday() == 4:  # Saturday
        if days_difference == 3:
            return True

    return False

if __name__ == "__main__":
    # Load the env file
    load_dotenv()
    # Replace with your Zoho CRM access token and the CSV file path
    access_token = os.environ.get("access_token")
    module_name = "deals"
    subject = os.environ.get("subject")
    body = os.environ.get("body")
    recipients = os.environ.get("recipients")
    sender_email = os.environ.get("sender_email")
    sender_password = os.environ.get("sender_password")
    smtp_server = os.environ.get("smtp_server")  # Use the SMTP server of your email provider
    smtp_port = os.environ.get("smtp_port")  # Use the appropriate SMTP port, for Gmail it's 587
    record = lc.get_latest_record_from_module(access_token, module_name)

    if should_send_email(record):
        print("Send email")
        se.send_email(subject, body, recipients, sender_email, sender_password, smtp_server, smtp_port)
    else:
        print("Do not send email")
