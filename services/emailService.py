import smtplib
from email.message import EmailMessage


SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USERNAME = "rrsweeden40@gmail.com"
SMTP_PASSWORD = "RR1RR2RR3"


def sendEmail(to: str):

    message = EmailMessage()

    message["From"] = SMTP_USERNAME
    message["To"] = to
    message["Subject"] = "Password Reset"

    message.set_content(
        f"""
Hello user,

We received a request to reset your password.

Your password reset request has been received.

Thank you.
"""
    )

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:

        server.starttls()

        server.login(
            SMTP_USERNAME,
            SMTP_PASSWORD
        )

        server.send_message(message)