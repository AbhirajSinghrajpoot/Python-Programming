import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/421e6d158f355f5e0c0f10b88fdb3f1f/flightDeals/prices"

USERS_ENDPOINT = "https://api.sheety.co/421e6d158f355f5e0c0f10b88fdb3f1f/flightDeals/user"

headers = {
    "Authorization": "Bearer flightDealsToken123"
}

class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):

        response = requests.get(
            url=SHEETY_PRICES_ENDPOINT,
            headers=headers
        )

        data = response.json()

        self.destination_data = data["prices"]

        return self.destination_data

    def update_destination_codes(self):

        for city in self.destination_data:

            new_data = {
                "price": {
                    "iataCode": city["iataCode"],
                    "airportName": city["airportName"],
                    "country": city["country"],
                    "timezone": city["timezone"]
                }
            }

            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=headers
            )

            print(response.text)

    def get_customer_emails(self):

        response = requests.get(
            url=USERS_ENDPOINT,
            headers=headers
        )

        data = response.json()

        return data["user"]