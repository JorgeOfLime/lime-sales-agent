from openai import OpenAI
client = OpenAI()

def generate_email(contact_name, goal_link):
    prompt = f"""
    Write a friendly, professional outreach email to {contact_name}, encouraging them to visit this page and get started: {goal_link}.
    Keep it short and persuasive.
    """
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content