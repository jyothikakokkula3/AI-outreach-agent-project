import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_email(company):

    prompt = f"""
    You are writing a professional outreach email.

    You are NOT part of the organisation.

    Organisation researched:
    {company['name']}

    Research information:
    {company['research']}

    Write an outreach email proposing collaboration with the organisation.
    Do not pretend you work for them.
    Keep the email concise and professional.
    """

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return completion.choices[0].message.content