import requests

response = requests.get(
    "https://api.open-meteo.com/v1/forecast",
    params={
        "latitude": 6.9271,
        "longitude": 79.8612,
        "current_weather": True
    }
)

data = response.json()

print(data)