import os
import requests

BASE_URL = "http://4.224.186.213/evaluation-service"

TOKEN = os.getenv("ACCESS_TOKEN")

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}


def get_depots():
    response = requests.get(
        f"{BASE_URL}/depots",
        headers=headers
    )
    response.raise_for_status()
    return response.json()


def get_vehicles():
    response = requests.get(
        f"{BASE_URL}/vehicles",
        headers=headers
    )
    response.raise_for_status()
    return response.json()