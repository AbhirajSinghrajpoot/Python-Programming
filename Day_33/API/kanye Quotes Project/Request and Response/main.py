import requests

url = "https://api.wheretheiss.at/v1/satellites/25544"

response = requests.get(url, timeout=10)

response.raise_for_status()

data = response.json()

latitude = data["latitude"]
longitude = data["longitude"]

iss_position = (latitude, longitude)

print(iss_position)