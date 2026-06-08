import os
import requests
from dotenv import load_dotenv

load_dotenv()

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = os.getenv("OWM_API_KEY")

weather_params = { 
    "lat": 51.5074,
    "lon": -0.1278, 
    "appid": API_KEY 
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

weather_slice = weather_data["list"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True
        
if will_rain:
    print("Bring an umbrella.")

