from crm.followupboss_client import get_contacts
import requests
import os
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

def get_single_person(person_id):
    url = f"{FUB_BASE_URL}/people/{person_id}"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def run():
    print("🚀 Fetching contacts from FollowUpBoss...")
    contacts = get_contacts()
    people = contacts.get("people", [])

    if not people:
        print("⚠️ No people found in FollowUpBoss.")
        return

    first_person = people[0]
    person_id = first_person.get("id")
    name = first_person.get("name", "Unnamed")

    print(f"✅ Found person: {name} (ID: {person_id})")
    print(f"🔍 Fetching full profile for {name}...")
    profile = get_single_person(person_id)
    print("✅ Got full profile JSON:")
    print(profile)

if __name__ == "__main__":
    run()
