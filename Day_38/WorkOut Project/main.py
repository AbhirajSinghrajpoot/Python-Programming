import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ["API_NINJAS_KEY"]
SHEET_ENDPOINT = os.environ["YOUR_SHEET_ENDPOINT"]
TOKEN = os.environ["TOKEN"]

exercise_endpoint = "https://api.api-ninjas.com/v1/caloriesburned"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "X-Api-Key": API_KEY
}

params = {
    "activity": exercise_text
}

response = requests.get(
    exercise_endpoint,
    headers=headers,
    params=params
)

result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y") 
now_time = datetime.now().strftime("%X")

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

bearer_headers = {
    "Authorization": f"Bearer {TOKEN}"
}

exercise = result[0]

sheet_inputs = {
    "workout": {
        "date": today_date,
        "time": now_time,
        "exercise": exercise["name"].title(),
        "duration": exercise["duration_minutes"],
        "calories": exercise["calories_per_hour"]
    }
}

sheet_response = requests.post(
    SHEET_ENDPOINT,
    json=sheet_inputs,
    headers=bearer_headers
)

print(sheet_response.text)
