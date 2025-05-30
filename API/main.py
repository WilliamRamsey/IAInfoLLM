from os import environ
from dotenv import load_dotenv
from Job import *
from Agent import *

# Load environmental variables stored in .env
load_dotenv()

# Instantiate Canidate
myJobDesires = JobDesires(100000, "Atlanta", "AI takeover defense engineer", "Sit in a server room with a bucket of water in case things get hairy.", "Relaxed ideally.", "Throw water on servers if AI decides to takeover humanity.")
myQualifications = Qualifications(["OfferDox: Software Development Intern (May 2024 - Present)"], ["Purdue University: BS in Computer Engineering"], ["Python", "Java", "Water Pumping"])
myCanidate = Candidate("William Ramsey", "williamdawsonramsey@gmail.com", myJobDesires, myQualifications)

# Instantiate canidate agent
myCanidateAgent = CandidateAgent(myCanidate, str(environ.get("GOOGLE_API_KEY")))

# Command line input
while True:
    prompt = input("> ")
    message = Message("Candidate", "Agent", prompt)
    print(myCanidateAgent.get_response(message))

