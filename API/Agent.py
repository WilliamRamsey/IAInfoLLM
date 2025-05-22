from google import genai
from Job import Job
from typing import List, Dict, Optional
from Candidate import Candidate
from dataclasses import dataclass

class Agent:
    """
    AI agent powered by Google's Gemini model for handling conversations and negotiations.
    
    
    This class represents an AI agent that can maintain conversation context, handle
    behavioral instructions, and interact with users through the Gemini language model.
    The agent's behavior is determined by its context and instructions.

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
    # def __init__(self, gemini_api_key: str, candidate: Candidate, prospective_jobs: List[Job]) -> None:
    def __init__(self, gemini_api_key: str) -> None:
        self.__client = genai.Client(api_key=gemini_api_key)

        self.__behavioral_instructions = "You are a professional job searching agent."
        self.__conversation_history: List[Dict[str, str]] = []

        # self.__context = [self.__behavioral_instructions, str(self.__canidate), [str(job) for job in prospective_jobs] self.__conversation_history]
        self.__context = [self.__behavioral_instructions, str(self.__conversation_history)]
    
    def get_response(self, prompt: str, role: str = "agent") -> str:
        """Generate a response using the Gemini model based on the current context and prompt.
        
        Args:
            prompt (str): The input prompt to generate a response for.
            role (str): The role of the speaker (default: "agent").

        Returns:
            str: The generated response from the Gemini model.

        Note:
            This method automatically adds both the prompt and response to the
            conversation history and context.
        """
        # Add the prompt to conversation history
        self.add_conversation(role, prompt)
        
        # Get response from Gemini
        response = self.__client.models.generate_content(
            model="gemini-2.0-flash-001",
            contents=self.__context
        )
        response_text = str(response.text)
        
        # Add the response to conversation history
        self.add_conversation("agent", response_text)
        
        return response_text

    def add_conversation(self, role: str, message: str) -> None:
        """Add a conversation entry to the agent's history.
        
        Args:
            role (str): Who is speaking ('candidate', 'recruiter', 'agent')
            message (str): The message content
        """
        self.__conversation_history.append({
            'role': role,
            'message': message
        })

    def get_conversation_history(self) -> List[Dict[str, str]]:
        """Get the agent's conversation history.
        
        Returns:
            List[Dict[str, str]]: List of conversation entries, each containing
                timestamp, role, and message.
        """
        return self.__conversation_history

    def update_behavioral_instructions(self, new_instructions: str) -> None:
        """Update the agent's behavioral instructions.
        
        Args:
            new_instructions (str): New instructions that define the agent's behavior.
        """
        self.__behavioral_instructions = new_instructions
        # Update the first context item (behavioral instructions)
        if self.__context:
            self.__context[0] = new_instructions
        else:
            self.add_context(new_instructions)


class RecruiterAgent(Agent):
    """AI agent specialized for recruiting and job matching.
    
    This agent represents a recruiter in the system, capable of searching through
    candidate profiles and engaging in negotiations. It inherits the base Agent
    capabilities and adds recruiting-specific context and behaviors.

    Args:
        jobs (List[Job]): List of available job positions to match with candidates.
        gemini_api_key (str): API key for accessing the Google Gemini service.
    """
    def __init__(self, jobs: List[Job], gemini_api_key: str) -> None:
        super().__init__(gemini_api_key, "") # Add recruiter-specific behavioral rules


class CandidateAgent(Agent):
    """AI agent specialized for job searching and candidate representation.
    
    This agent represents a job seeker in the system, capable of searching through
    job listings and engaging in negotiations with recruiters. It inherits the base
    Agent capabilities and adds candidate-specific context and behaviors.

    Args:
        candidate (Candidate): The candidate profile this agent represents.
        gemini_api_key (str): API key for accessing the Google Gemini service.
    """
    def __init__(self, candidate: Candidate, gemini_api_key: str) -> None:
        super().__init__(gemini_api_key, "") # Add candidate-specific behavioral rules
    
    def query_jobs(self) -> List[Job]:
        """Search for jobs matching the candidate's preferences.
        
        Returns:
            List[Job]: List of job positions that match the candidate's criteria.

        Raises:
            NotImplementedError: If job search functionality is not implemented.

        Note:
            This method is a placeholder and needs to be implemented with actual
            job search logic based on the candidate's preferences.
        """
        raise NotImplementedError("Job search functionality not implemented yet")