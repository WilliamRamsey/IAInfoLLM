from os import environ
from dotenv import load_dotenv

from google import genai
from google.genai import types

from Job import Job

# Load environmental variables stored in .env
load_dotenv()

# Creates Google Cloud Client
client = genai.Client(api_key = environ.get("GOOGLE_API_KEY"))

# Add job information to context
job1 = Job("Software Engineer", "Microsoft", 120000, "You write code for copilot.")
job1.save()
context = [str(job) for job in Job.jobs_from_file()]
context.append("You are a customer support chat bot for a job searching company.")

while True:
    prompt = input("> ")
    context.append(prompt)
    response = client.models.generate_content(
        model = "gemini-2.0-flash-001",
        contents = context
    )
    context.append(response.text)
    print(response.text)
