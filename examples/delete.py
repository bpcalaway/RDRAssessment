import requests
import json

# We're deleting whatever the db is calling the first entry here, don't care too much what it is
user_1_data = json.loads(requests.get("http://localhost:8080/list?user_id=1").content)

id = user_1_data[0].get("id", None)
print(f"Deleting entry with ID {id}...")
requests.delete("http://localhost:8080/event", data={"id": id})
