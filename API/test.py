from os import environ
from dotenv import load_dotenv

from Agent import *
load_dotenv()

api_key = environ.get("GOOGLE_API_KEY")
myAgent = Agent(api_key)

print(myAgent.get_response(content = "Hello world", sender="User", recipient="Agent"))
