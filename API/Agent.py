from google import genai
from google.genai import types
from typing import List
from Candidate import *
from dataclasses import dataclass

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
        self.__client = genai.Client(api_key=gemini_api_key)

        self.__behavioral_instructions = "Respoond to the last message in the conversation."
        self.__conversation_history: List[Message] = []    

    @property
    def context(self):
        """
        Get the current context for the agent.

        Returns:
            List[str]: A list containing the behavioral instructions and the formatted conversation history string.
        """
        return [self.__behavioral_instructions, self.get_conversation_history_str()]

    def get_response(self, message: Message) -> str:
        """
        Gets a response from gemini

        Args:
            message (Message): Message to send
        
        Returns:
            AI model response.
        """
        self.add_conversation(message)
        
        # Get response from Gemini
        # TODO consider removing cast to list
        response = self.__client.models.generate_content(model = "gemini-2.0-flash-001", contents = self.context)
        response_text = str(response.text)
        
        # Add the response to conversation history
        # TODO add cases that allow for more than a two way conversation. IE user sends to agent, agent sends to all
        response_message = Message(sender = message.recipient, recipient = message.sender, content = response_text)
        self.add_conversation(response_message)

        return response_text

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
    def __init__(self, candidate: Candidate, gemini_api_key: str) -> None:
        super().__init__(gemini_api_key)
        self.__candidate = candidate
        self.__position_shortlist = []
        self.__position_offers = []
        self.update_behavioral_instructions("You are an agent representing a job searching candidate. Determine and save the candidates ideal location and salary.")
    
    @property
    def context(self) -> list[str]:
        return [super().get_behavioral_instructions(), str(self.__candidate), super().get_conversation_history_str()]
    
    def set_desired_location(self, location: str) -> None:
        self.__candidate.__job_desires.location = location
    
    def set_desired_salary(self, salary: int) -> None:
        self.__candidate.__job_desires.salary = salary

class RecruitingAgent(Agent):
    """
    
    """
    def __init__(self, gemini_api_key: str) -> None:
        super().__init__(gemini_api_key)
        self.__candidate_short_list = []
        self.__secured_candidate = []
        self.update_behavioral_instructions("")
    
    