import requests
import json

party_data = json.loads(
    requests.get("http://localhost:8080/search?keyword=Party").content
)

print(f"Found entries with 'Party' in the title: {len(party_data)}")
print(party_data)
