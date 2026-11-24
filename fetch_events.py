import json
import os
import requests

TOKEN = os.environ["DX_TOKEN"]

url = "https://public.dx.no/v1/partners/155/events?page=1&size=20"

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "accept": "application/json"
}

response = requests.get(url, headers=headers)
response.raise_for_status()

data = response.json()

with open("events.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("events.json oppdatert")
