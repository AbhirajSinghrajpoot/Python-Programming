from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
import requests

USERS_ENDPOINT = "https://api.sheety.co/421e6d158f355f5e0c0f10b88fdb3f1f/flightDeals/users"

headers = {
    "Authorization": "Bearer flightDealsToken123"
}

print("Welcome to Abhiraj's Flight Club.")
print("We find the best flight deals and email you.\n")

first_name = input("What is your first name?\n")
last_name = input("What is your last name?\n")

email = input("What is your email?\n")
confirm_email = input("Type your email again.\n")

if email == confirm_email:

    user_data = {
        "user": {
            "firstName": first_name,
            "lastName": last_name,
            "email": email
        }
    }

    response = requests.post(
        url=USERS_ENDPOINT,
        json=user_data,
        headers=headers
    )

    print(response.text)
    print("You're in the club!\n")

else:
    print("Emails do not match.")
    exit()

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
users = data_manager.get_customer_emails()

flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "LON"

if sheet_data[0]["iataCode"] == "":

    for row in sheet_data:

        airport_info = flight_search.get_destination_code(
            row["city"]
        )

        if airport_info:

            row["iataCode"] = airport_info["iataCode"]
            row["airportName"] = airport_info["airportName"]
            row["country"] = airport_info["country"]
            row["timezone"] = airport_info["timezone"]

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)

six_month_from_today = (
    datetime.now() + timedelta(days=(6 * 30))
)

for destination in sheet_data:

    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

    if flight is None:
        continue

    if flight.price < destination["lowestPrice"]:

        google_flight_link = (
            f"https://www.google.com/travel/flights?"
            f"hl=en#flt="
            f"{flight.origin_airport}."
            f"{flight.destination_airport}."
            f"{flight.out_date}*"
            f"{flight.destination_airport}."
            f"{flight.origin_airport}."
            f"{flight.return_date}"
        )

        message = (
            f"✈️ Low Price Alert!\n\n"
            f"Only £{flight.price}\n\n"
            f"From: {flight.origin_city} "
            f"({flight.origin_airport})\n"
            f"To: {flight.destination_city} "
            f"({flight.destination_airport})\n\n"
            f"Departure: {flight.out_date}\n"
            f"Return: {flight.return_date}\n\n"
            f"Book here:\n{google_flight_link}"
        )

        notification_manager.send_sms(
            message=message
        )

        email_list = [
            row["email"]
            for row in users
        ]

        notification_manager.send_emails(
            email_list=email_list,
            message=message
        )