from crm.followupboss_client import get_contacts, add_note_to_contact
# from agents.email_agent import generate_email
# from agents.sms_agent import generate_sms
# from agents.call_script_agent import generate_call_script
from agents.email_agent_local import generate_email
from agents.sms_agent_local import generate_sms
from agents.call_script_local import generate_call_script

GOAL_LINK = "https://limecreativedesign.com/quote"

def run():
    contacts = get_contacts(tag="Prospect")
    
    for person in contacts.get("people", []):
        name = person.get("name", "there")
        person_id = person.get("id")

        """
        email_content = generate_email(name, GOAL_LINK)
        sms_content = generate_sms(name, GOAL_LINK)
        call_script = generate_call_script(name, GOAL_LINK)

        print("\n================================")
        print(f"Contact: {name}")
        print(f"EMAIL:\n{email_content}")
        print(f"SMS:\n{sms_content}")
        print(f"CALL SCRIPT:\n{call_script}")

        # Example: log note back to CRM
        add_note_to_contact(person_id, "AI outreach prepared with email/SMS/call script.")
        """
        email = generate_email(name, GOAL_LINK)
        sms = generate_sms(name, GOAL_LINK)
        call_script = generate_call_script(name, GOAL_LINK)

        print("\n================================")
        print(f"Contact: {name}")
        print(f"EMAIL:\n{email}")
        print(f"SMS:\n{sms}")
        print(f"CALL SCRIPT:\n{call_script}")

        add_note_to_contact(person_id, "AI outreach planned - using local template version.")

if __name__ == "__main__":
    run()
