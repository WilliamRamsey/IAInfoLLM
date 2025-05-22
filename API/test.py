from Agent import *
from Candidate import * 

"""
conversation = [{"role": "William", "message": "hey"}, {"role": "recruiter", "message": "whats up"}]
print([f"{line["role"]}: {line["message"]}" for line in conversation])
print(conversation)
"""

myRecruiter = Agent("AIzaSyAViHH6WvYbY_2LbALBBIM1rXAcA9wM_gI")
myRecruiter.get_response("Hello. How are you?")