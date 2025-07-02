## sales_ai_agent/test_connections.py
import os
import base64
import requests
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# FollowUpBoss test
FUB_API_KEY = os.getenv("FUB_API_KEY")
auth_string = f"{FUB_API_KEY}:".encode("utf-8")
auth_base64 = base64.b64encode(auth_string).decode("utf-8")
headers = {
    "Authorization": f"Basic {auth_base64}",
    "Content-Type": "application/json"
}
response = requests.get("https://api.followupboss.com/v1/people", headers=headers)
if response.status_code == 200:
    print("✅ Successfully connected to FollowUpBoss API.")
else:
    print("❌ FUB connection failed:", response.status_code, response.text)

# OpenAI test
client = OpenAI()
try:
    chat = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Say hello!"}]
    )
    print("✅ Successfully connected to OpenAI. Response:", chat.choices[0].message.content)
except Exception as e:
    print("❌ OpenAI connection failed:", e)