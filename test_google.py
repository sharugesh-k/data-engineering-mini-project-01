import requests

try:
    r = requests.get("https://www.google.com", timeout=10)
    print(r.status_code)
except Exception as e:
    print(e)