import requests
import os
import random
from dotenv import load_dotenv
from flight_data import FlightData

load_dotenv()

API_KEY = os.environ["AVIATIONSTACK_API_KEY"]

AVIATIONSTACK_ENDPOINT = "http://api.aviationstack.com/v1/airports"


class FlightSearch:
    def get_destination_code(self, city_name):

        params = {
            "access_key": API_KEY,
            "search": city_name
        }

        response = requests.get(
            AVIATIONSTACK_ENDPOINT,
            params=params
        )

        data = response.json()

        try:

            airport_data = {
                "iataCode": data["data"][0]["iata_code"],
                "airportName": data["data"][0]["airport_name"],
                "country": data["data"][0]["country_name"],
                "timezone": data["data"][0]["timezone"],
            }

            return airport_data

        except IndexError:
            print(f"No airport found for {city_name}")
            return None



    def check_flights(
        self,
        origin_city_code,
        destination_city_code,
        from_time,
        to_time
    ):

        import random

        estimated_price = random.randint(80, 350)

        flight_data = FlightData(
            price=estimated_price,
            origin_city="London",
            origin_airport=origin_city_code,
            destination_city=destination_city_code,
            destination_airport=destination_city_code,
            out_date=from_time.strftime("%Y-%m-%d"),
            return_date=to_time.strftime("%Y-%m-%d")
        )

        print(
            f"{destination_city_code}: £{estimated_price}"
        )

        return flight_data
