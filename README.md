🚀 Lime Design AI Sales Outreach Agent
This is an automated outreach assistant for Lime Design that:

- Generates personalized emails, SMS drafts, and call scripts for leads in FollowUpBoss
- Sends actual outreach emails using Gmail (with app password authentication)
- Logs all outreach activities to outreach_log.csv for records and future review
- Sends a summary email report after each run

Future updates will also include direct SMS sending capabilities (e.g. via Betty or Twilio).


⚙️ Setup Instructions
1. Install Python dependencies

    Make sure you're inside the project folder. Then install the dependencies inside your virtual environment (or globally):

        'pip install -r requirements.txt'

2. Configure your .env file

    Your .env file should look like this (edit with your credentials):

        FUB_API_KEY=your_followupboss_api_key
        OPENAI_API_KEY=your_openai_api_key

        EMAIL_HOST=smtp.gmail.com
        EMAIL_PORT=587
        EMAIL_USER=your_email@limecreativedesign.com
        EMAIL_PASSWORD=your_gmail_app_password

        DRY_RUN=False
        TEST_EMAIL=your_email@limecreativedesign.com

    Note:
    - EMAIL_USER and EMAIL_PASSWORD are currently set to use create@limecreativedesign.com and its generated Gmail App Password.
    - This can remain as is if preferred. If you’d like to switch to another sending email, Jorge can assist with setup.

    DRY_RUN: Set to True if you want to only print the outreach (without sending emails).

    TEST_EMAIL: While testing, all emails are redirected here instead of real clients. Remove or comment this line when ready for live sending.

3. Run the outreach

     'python run.py'

    This will pull all contacts from FollowUpBoss, generate outreach materials, send emails, log everything, and send you a summary report.


🛠️ Notes for production
Before sending live outreach to clients:

- Make sure DRY_RUN=False
- Remove or comment out the TEST_EMAIL=... line in .env so emails go directly to clients.

All outreach is logged in outreach_log.csv for accountability.


🚀 Upcoming Features

    SMS API Integration
        Future versions will integrate with services like Betty or Twilio to automatically send SMS messages in addition to emails.