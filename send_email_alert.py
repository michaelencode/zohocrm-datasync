import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

def send_email(subject, body, recipients, sender_email, sender_password, smtp_server, smtp_port):
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = ', '.join(recipients)
    msg['Subject'] = subject

    # Attach the body text to the email message
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, recipients, msg.as_string())

        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        server.quit()

if __name__ == "__main__":
    # Load the env file
    load_dotenv()
    # Replace with your Zoho CRM access token and the CSV file path

    subject = os.environ.get("subject")
    body = os.environ.get("body")
    recipients = os.environ.get("recipients")
    sender_email = os.environ.get("sender_email")
    sender_password = os.environ.get("sender_password")
    smtp_server = os.environ.get("smtp_server")  # Use the SMTP server of your email provider
    smtp_port = os.environ.get("smtp_port")  # Use the appropriate SMTP port, for Gmail it's 587

    send_email(subject, body, recipients, sender_email, sender_password, smtp_server, smtp_port)

