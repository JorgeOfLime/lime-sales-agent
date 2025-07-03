from openai import OpenAI
client = OpenAI()

def generate_call_script(contact_name, goal_link):
    prompt = f"""
    Draft a short call script for reaching out to {contact_name}, encouraging them to visit {goal_link} to get started. Include a greeting, reason for call, and gentle push to complete the form.
    """
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content