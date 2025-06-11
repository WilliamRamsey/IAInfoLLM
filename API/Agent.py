from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List
from google import genai
from google.genai import types
from Candidate import *
from Gemini_Functions import *

"""
# Context format
Behavioral instructions (paragraph)

Canidate attributes

Job listings (Do we pass a special search function? Just pass all jobs as list?)

Conversation history

"""

@dataclass
class Message:
    """
    Represents a message used for prompting agents and storing a conversation history.
    """
    sender: str
    recipient: str
    content: str

@abstractmethod
class Agent:
    """
    A core class that manages the context for a Gemini Agent and allows for prompting with [Messages]
    It maintains generic behavioral instructions and a conversation history.
    The conversation history is stored as a list of [Messages]

    Attributes:
        __context (List[str]): List of conversation context items that provide
            behavioral rules and conversation history.
        __client (genai.Client): Google Gemini API client instance.
        __behavioral_instructions (str): Instructions that define how the agent should
            behave during conversations and negotiations.
        __conversation_history (List[Dict[str, str]]): Chronological record of all
            conversations. Each entry contains timestamp, role, and message.

    Args:
        gemini_api_key (str): API key for accessing the Google Gemini service.
    """
    def __init__(self, gemini_api_key: str) -> None:

        # Client instantiation
        self.__client = genai.Client(api_key=gemini_api_key)

        self.__behavioral_instructions = "Respond to the last message in the conversation. Ensure you call the provided setter functions whenever a user divuldges new information. Do not announce your function calls to the user. The conversation history is for your reference. Do not attempt to copy the to-from formatting it uses in your messages to the user."
        self.__conversation_history: List[Message] = []    

    @property
    def context(self):
        """
        Get the current context for the agent.

        Returns:
            List[str]: A list containing the behavioral instructions and the formatted conversation history string.
        """
        return [self.__behavioral_instructions, self.get_conversation_history_str()]

    
    def get_response(self, message: Message, functions = []) -> str:
        """
        Gets a response from gemini

        Args:
            message (Message): Message to send
        
        Returns:
            AI model response.
        """
        self.add_conversation(message)
        
        # Get response from Gemini
        # for when functions are passed. used in CandidateAgent overload
        if functions != []:
            tools = types.Tool(function_declarations=functions) # type: ignore
            config =  types.GenerateContentConfig(tools=[tools])
            response = self.__client.models.generate_content(model = "gemini-2.0-flash-001",
                                                            contents = self.context, # type: ignore
                                                            config = config)
        else:
            response = self.__client.models.generate_content(model = "gemini-2.0-flash-001",
                                                contents = self.context) # type: ignore

        # Check to see which function was called by model
        if not response.candidates[0].content.parts[0].function_call: #type: ignore
            response_text = str(response.text)
        
            # Add the response to conversation history
            # TODO add cases that allow for more than a two way conversation. IE user sends to agent, agent sends to all
            response_message = Message(sender = message.recipient, recipient = message.sender, content = response_text)
            self.add_conversation(response_message)

            return response_text
        
        else:
            return self.execute_gemini_function_calls(response)

    @abstractmethod
    def execute_gemini_function_calls(self, response) -> str:
        """
        This needs to be abstract because CandidateAgents and RecruitingAgents have different functions they can call.
        """
        pass

    def add_conversation(self, message) -> None:
        """
        Append a Message object to the agent's conversation history.

        Args:
            message (Message): The Message instance to add to the conversation history.
        """
        self.__conversation_history.append(message)

    def get_conversation_history_str(self) -> str:
        """
        Get the agent's conversation history as a formatted string.

        Returns:
            str: The conversation history, formatted as "From {sender} to {recipient}: {content}" per line.
        """
        conversation_string = ""
        for message in self.__conversation_history:
            conversation_string += f"From {message.sender} to {message.recipient}: {message.content}\n"
        return conversation_string

    def update_behavioral_instructions(self, new_instructions: str) -> None:
        """
        Append new instructions to the agent's behavioral instructions.

        This method is primarily intended for use by child classes to modify the instance's behavioral instruction string.

        Args:
            new_instructions (str): Instructions to supplement the default agent behaviors.
        """
        self.__behavioral_instructions += new_instructions

    def get_behavioral_instructions(self) -> str:
        """
        Returns the behavioral instructions given to gemini
        """
        return self.__behavioral_instructions

class CandidateAgent(Agent):
    """
    AI agent that represents a canidate as they search for jobs.

    Has access to the canidate's profile
    """
    __CandidateAgent_functions = [
        query_jobs_declaration,
        set_candidate_ideal_salary_declaration,
        set_candidate_minimum_salary_declaration,
        set_candidate_location_declaration,
        set_candidate_position_declaration,
        set_candidate_job_description_declaration,
        set_candidate_company_culture_declaration,
        set_candidate_responsibilities_declaration,
        set_candidate_work_experience_declaration,
        set_candidate_education_declaration,
        set_candidate_skills_declaration
    ]

    def __init__(self, candidate: Candidate, gemini_api_key: str) -> None:
        super().__init__(gemini_api_key)
        self.candidate = candidate
        self.__position_shortlist = []
        self.__position_offers = []
        self.update_behavioral_instructions("You are a job searching agent having a conversation with the candidate you represent. Your goal is to aquire information about a candidates qualifications and job desires, save this info with the setter functions, and help the candidate find a suitable job with the query_jobs function.")
    
    @property
    def context(self) -> list[str]:
        return [super().get_behavioral_instructions(), str(self.candidate), super().get_conversation_history_str()]
    
    def get_response(self, message: Message, functions = __CandidateAgent_functions) -> str:
        return super().get_response(message=message, functions=functions)

    def execute_gemini_function_calls(self, response) -> str:
        """
        Automatically updates the conversation history with the request message from AI to service and service to AI.
        Automatically reprompts AI with the response message from the service.
        Returns the final str response of the model once it has viewed the function response message.
        """

        # parse actual function call from response
        function_call = response.candidates[0].content.parts[0].function_call # type: ignore
        print(f"AGENT CALLED {function_call.name}({function_call.args})")

        # EXTREAMLY UNSAFE 
        # Basically lets gemini evalate functions completly unsupervised and unsanitized
        # A user could potentially evaluate whatever code they please with this by passing the correct arguments

        argument_string = ""
        for key, value in function_call.args.items():
            if type(value) == str:
                argument_string += f"{key} = \"{value}\", "
            else:
                argument_string += f"{key} = {value}, "
        argument_string = argument_string[:-2] # delete that last comma
        function_call_string = f"{function_call.name}({argument_string})"
        print(function_call_string)
        result = eval(function_call_string)
        request_message = Message("Agent", "API", function_call_string)
        response_message = Message("API", "Agent", result)
        self.add_conversation(request_message)
        return self.get_response(response_message)


        """
        if function_call.name == "query_jobs": # type: ignore
            # get arguments
            minimum_salary = function_call.args["minimum_salary"] # type: ignore
            location = function_call.args["location"] # type: ignore

            # Actually call the function with the arguments provided by LLM
            matching_jobs = Job.query_jobs(minimum_salary, location)

            # Update the conversation to include the agents request to the job 
            job_request_message = Message("Agent", "Job Database", f"query_jobs({minimum_salary}, {location})")
            job_response_message = Message("Job Database", "Agent", matching_jobs)
            self.add_conversation(job_request_message)
            # reprompt gemini with new message
            return self.get_response(job_response_message)
        
        elif function_call.name == "set_candidate_ideal_salary":
            # set the candidates ideal salary
            ideal_salary = function_call.args["ideal_salary"]
            self.__candidate.set_ideal_salary(ideal_salary)
            
            # update conversation history
            set_ideal_salary_message = Message("Agent", "Candidate Database", f"Candidate.set_ideal_salary({ideal_salary})")
            set_ideal_salary_response = Message("Candidate Database", "Agent", f"Successfully set salary to {ideal_salary}")
            self.add_conversation(set_ideal_salary_message)
            # reprompt
            return self.get_response(set_ideal_salary_response)
        
        else:
            return ""
        """

class RecruitingAgent(Agent):
    """
    
    """
    def __init__(self, gemini_api_key: str) -> None:
        super().__init__(gemini_api_key)
        self.__candidate_short_list = []
        self.__secured_candidate = []
        self.update_behavioral_instructions("")
    
