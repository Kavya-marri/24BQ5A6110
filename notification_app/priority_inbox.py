import requests

TOKEN = "YOUR_ACCESS_TOKEN"

URL = "http://4.224.186.213/evaluation-service/notifications"

headers = {
    "Authorization": f"Bearer {TOKEN}"
}

priority_map = {
    "Placement": 100,
    "Result": 70,
    "Event": 40
}

response = requests.get(URL, headers=headers)

data = response.json()

notifications = data["notifications"]

for notification in notifications:
    notification["priority"] = priority_map.get(
        notification["Type"],
        0
    )

top_notifications = sorted(
    notifications,
    key=lambda x: x["priority"],
    reverse=True
)[:10]

for notification in top_notifications:
    print(
        notification["Type"],
        notification["Message"],
        notification["priority"]
    )