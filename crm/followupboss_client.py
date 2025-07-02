import os
import requests
import base64
from dotenv import load_dotenv

load_dotenv()

FUB_API_KEY = os.getenv("FUB_API_KEY")
FUB_BASE_URL = "https://api.followupboss.com/v1"

auth_string = f"{FUB_API_KEY}:".encode("utf-8")
auth_base64 = base64.b64encode(auth_string).decode("utf-8")

headers = {
    "Authorization": f"Basic {auth_base64}",
    "Content-Type": "application/json"
}

def get_contacts(tag=None):
    url = f"{FUB_BASE_URL}/people"
    params = {"tag": tag} if tag else {}
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

def add_note_to_contact(person_id, note):
    url = f"{FUB_BASE_URL}/people/{person_id}/notes"
    data = {"body": note}
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()
