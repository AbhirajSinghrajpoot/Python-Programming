from twilio.rest import Client
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

TWILIO_SID = os.environ["TWILIO_SID"]

TWILIO_AUTH_TOKEN = os.environ["TWILIO_AUTH_TOKEN"]

TWILIO_VIRTUAL_NUMBER = os.environ["TWILIO_VIRTUAL_NUMBER"]

TWILIO_VERIFIED_NUMBER = os.environ["TWILIO_VERIFIED_NUMBER"]

MY_EMAIL = os.environ["MY_EMAIL"]

MY_PASSWORD = os.environ["MY_PASSWORD"]


class NotificationManager:

    def __init__(self):

        self.client = Client(
            TWILIO_SID,
            TWILIO_AUTH_TOKEN
        )

    def send_sms(self, message):

        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )

        print(message.sid)

    def send_emails(
        self,
        email_list,
        message
    ):

        with smtplib.SMTP(
            "smtp.gmail.com", 587
        ) as connection:

            connection.starttls()

            connection.login(
                user=MY_EMAIL,
                password=MY_PASSWORD
            )

            for email in email_list:

                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Flight Deal!\n\n{message}".encode("utf-8")
                )