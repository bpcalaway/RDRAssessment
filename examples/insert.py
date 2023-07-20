import requests

# When you run these, please make sure that you have the app running and bound to localhost:8080

all_data = [
    {"user_id": 1, "title": "Sample", "description": ""},
    {"user_id": 1, "title": "Retirement Party", "description": "party for Paul"},
    {"user_id": 1, "title": "All Hands", "description": "Mandatory"},
    {
        "user_id": 2,
        "title": "Independence Day",
        "description": "Time off scheduled for  7/04/2099",
    },
    {
        "user_id": 2,
        "title": "New Years Party",
        "description": "Work party scheduled for 12/31/2099",
    },
]

for data in all_data:
    requests.post("http://localhost:8080/event", data=data)
