import sys
import os
import csv
import emailer

# Print loaded environment right away
print("\n🎯 ==============================")
print(f"✅ RUNNING TEST SCRIPT ENVIRONMENT")
print(f"- DRY_RUN: {emailer.DRY_RUN}")
print(f"- TEST_EMAIL: {emailer.TEST_EMAIL}")
print(f"- EMAIL_USER: {emailer.EMAIL_USER}")
print(f"- EMAIL_PASSWORD: {'***' if emailer.EMAIL_PASSWORD else None}")
print("🎯 ==============================\n")

from emailer import send_email, send_summary_email
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

    if not people:
        print("⚠️ No contacts found in FollowUpBoss.")
        return

    # Limit to first 3 contacts
    test_people = people[:3]

    total_contacts = 0
    emails_sent = 0
    skipped_contacts = 0
    recipients = []

    print(f"✅ Retrieved {len(test_people)} contacts for this test run.")

    for person in test_people:
        total_contacts += 1
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

        if person.get("emails"):
            to_address = person["emails"][0]["value"]
            send_email(to_address, "Ready to take the next step?", email_copy)
            emails_sent += 1
            recipients.append(f"- {name} <{to_address}>")
        else:
            print(f"⚠️ No email found for {name}, skipping send.")
            skipped_contacts += 1

        save_contact_log(person, email_copy, sms, call_script)
        print("✅ Logged this outreach plan to outreach_log.csv.")

    # Build the summary email body
    summary_body = f"""
    Lime Design Outreach Summary (TEST):

    - Contacts processed: {total_contacts}
    - Emails sent: {emails_sent}
    - Skipped (missing emails): {skipped_contacts}

    Recipients:
    {"\n".join(recipients)}

    Thank you for using the Lime Design AI Sales Agent.
    """

    print("\n========================================")
    print("✅ Outreach Summary (TEST):")
    print(summary_body)
    print("========================================")

    send_summary_email("Lime Design Outreach Summary Report (TEST)", summary_body)

if __name__ == "__main__":
    run()
