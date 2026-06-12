import requests

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(
    "https://api.open-meteo.com/v1/forecast",
    params={
        "latitude": 52.52,
        "longitude": 13.41,
        "hourly": "temperature_2m"
    },
    headers=headers,
    timeout=15
)

print(response.status_code)
print(response.text[:200])