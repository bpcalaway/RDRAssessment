import requests
import json

user_1_data = json.loads(requests.get("http://localhost:8080/list?user_id=1").content)
user_2_data = json.loads(requests.get("http://localhost:8080/list?user_id=2").content)

print(
    f"Testing for correct numbers of entries: {len(user_1_data) == 3 and len(user_2_data) == 2}"
)
print(f"User 1: {user_1_data}")
print(f"User 2: {user_2_data}")
