import sys
import os
import csv

# Ensure your project directory is in Python path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from crm.followupboss_client import get_contacts
from agents.email_agent_local import generate_email
from agents.sms_agent_local import generate_sms
from agents.call_script_local import generate_call_script

GOAL_LINK = "https://limecreativedesign.com/quote"

def save_contact_log(person, email_copy, sms, call_script):
    emails = ", ".join([e.get("value") for e in person.get("emails", [])])
    phones = ", ".join([p.get("value") for p in person.get("phones", [])])

    file_exists = os.path.isfile("outreach_log.csv")
    with open("outreach_log.csv", "a", newline='', encoding='utf-8') as csvfile:
        fieldnames = ["ID", "Name", "Email(s)", "Phone(s)", "Email Copy", "SMS Copy", "Call Script Copy"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerow({
            "ID": person.get("id"),
            "Name": person.get("name"),
            "Email(s)": emails,
            "Phone(s)": phones,
            "Email Copy": email_copy.strip(),
            "SMS Copy": sms.strip(),
            "Call Script Copy": call_script.strip()
        })

def run():
    print("🚀 Fetching ALL contacts from FollowUpBoss...")
    contacts = get_contacts()
    people = contacts.get("people", [])

    print(f"✅ Retrieved {len(people)} total contacts.")

    if not people:
        print("⚠️ No contacts found in FollowUpBoss. Add some leads to test.")
        return

    for person in people:
        name = person.get("name", "there")
        emails = ", ".join([e.get("value") for e in person.get("emails", [])])
        phones = ", ".join([p.get("value") for p in person.get("phones", [])])

        email_copy = generate_email(name, GOAL_LINK)
        sms = generate_sms(name, GOAL_LINK)
        call_script = generate_call_script(name, GOAL_LINK)

        print("\n================================")
        print(f"Contact: {name}")
        print(f"Email Address(es): {emails}")
        print(f"Phone Number(s): {phones}")
        print(f"EMAIL:\n{email_copy}")
        print(f"SMS:\n{sms}")
        print(f"CALL SCRIPT:\n{call_script}")

        save_contact_log(person, email_copy, sms, call_script)
        print("✅ Logged this outreach plan to outreach_log.csv.")

if __name__ == "__main__":
    run()