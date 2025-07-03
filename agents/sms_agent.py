from openai import OpenAI
client = OpenAI()

def generate_sms(contact_name, goal_link):
    prompt = f"""
    Write a very short SMS to {contact_name}, reminding them to complete the quote or NDA here: {goal_link}.
    Be friendly and include a call to action.
    """
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content