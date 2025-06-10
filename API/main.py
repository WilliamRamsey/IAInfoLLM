from os import environ
from dotenv import load_dotenv
from Job import *
from Agent import *
from Gemini_Functions import *

"""
# New user workflow
Landing page 
Instantiates empty candidate.
Instantiates new Candidate agent.
Agent calls setter instance methods of the candidate to update information.
"""

# Load environmental variables stored in .env
load_dotenv()

# Instantiate Canidate
myJobDesires = JobDesires(100000, 75000, "Atlanta", "Software Developer")
myQualifications = Qualifications(["Purdue CS Teaching Assistant", "Microsoft Backend Developer"], ["BS in Computer Engineering - Purdue University"], ["Python", "Java", "C++"])

myCanidate = Candidate("William Ramsey", "williamdawsonramsey@gmail.com", myJobDesires, myQualifications)

# Instantiate canidate agent
myCanidateAgent = CandidateAgent(myCanidate, str(environ.get("GOOGLE_API_KEY")))

# Command line input
while True:
    prompt = input("> ")
    message = Message("Candidate", "Agent", prompt)
    print(myCanidateAgent.get_response(message))
