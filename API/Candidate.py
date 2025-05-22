from __future__ import annotations
from typing import Optional, List, Dict
from dataclasses import dataclass
from datetime import datetime
from Agent import Agent
from Job import Job

@dataclass
class JobDesires:
    """Standard and semantic job preferences for a candidate"""
    # Standard query attributes
    salary: Optional[int] = None
    location: Optional[str] = None
    position: Optional[str] = None
    description: Optional[str] = None
    
    # Semantic attributes
    company_culture: Optional[str] = None
    responsibilities: Optional[str] = None

@dataclass
class Qualifications:
    """Candidate's work experience and qualifications"""
    work_experience: List[str]  # List of work experiences with company, role, duration, etc.
    education: List[str]  # List of educational qualifications
    skills: List[str]  # List of technical and soft skills

class Candidate:
    """
    Represents a job candidate with their preferences, qualifications, and AI agent.
    This class implements the structure shown in the system diagram.
    """
    __candidate_count = 0

    def __init__(
        self,
        name: str,
        email: str,
        gemini_api_key: str,
        job_desires: Optional[JobDesires] = None,
        qualifications: Optional[Qualifications] = None,
        soft_info: Optional[str] = None,
        id: Optional[int] = None
    ) -> None:
        """
        Initialize a new candidate with their basic information and preferences.
        
        Args:
            name: Candidate's full name
            email: Candidate's email address
            gemini_api_key: API key for the Gemini AI service
            job_desires: Optional job preferences
            qualifications: Optional work experience and qualifications
            soft_info: Optional text embedding of soft information
            id: Optional unique identifier
        """
        if id is None:
            Candidate.__candidate_count += 1
            self.__id = Candidate.__candidate_count
        else:
            self.__id = id

        self.__name = name
        self.__email = email
        self.__job_desires = job_desires or JobDesires()
        self.__qualifications = qualifications or Qualifications([], [], [])
        self.__soft_info = soft_info
        self.__offers: List[Job] = []  # List of job offers received
        
        # Initialize the agent with candidate-specific instructions
        behavioral_instructions = (
            f"You are an AI agent representing {name}, a job candidate. "
            "Your role is to help find suitable job opportunities and negotiate on their behalf. "
            "Always maintain professionalism and prioritize the candidate's best interests."
        )
        self.__agent = Agent(gemini_api_key, behavioral_instructions)

    def get_agent(self) -> Agent:
        """Get the candidate's AI agent.
        
        Returns:
            Agent: The AI agent representing this candidate.
        """
        return self.__agent

    def add_offer(self, offer: Dict) -> None:
        """
        Add a job offer to the candidate's list of offers.
        
        Args:
            offer: Dictionary containing offer details
        """
        self.__offers.append({
            'timestamp': datetime.now().isoformat(),
            **offer
        })

    def update_job_desires(self, **kwargs) -> None:
        """
        Update the candidate's job desires.
        
        Args:
            **kwargs: Key-value pairs of job desire attributes to update
        """
        for key, value in kwargs.items():
            if hasattr(self.__job_desires, key):
                setattr(self.__job_desires, key, value)

    def add_work_experience(self, experience: Dict[str, str]) -> None:
        """
        Add a work experience entry to qualifications.
        
        Args:
            experience: Dictionary containing work experience details
        """
        self.__qualifications.work_experience.append(experience)

    def add_education(self, education: Dict[str, str]) -> None:
        """
        Add an education entry to qualifications.
        
        Args:
            education: Dictionary containing education details
        """
        self.__qualifications.education.append(education)

    def add_skill(self, skill: str) -> None:
        """
        Add a skill to qualifications.
        
        Args:
            skill: Skill to add
        """
        if skill not in self.__qualifications.skills:
            self.__qualifications.skills.append(skill)

    def get_offers(self) -> List[Job]:
        """Get all offers received by the candidate."""
        return self.__offers

    def __str__(self) -> str:
        """String representation of the candidate."""
        return f"Candidate {self.__id}: {self.__name} ({self.__email})"

    def save(self) -> None:
        """Save the candidate's information to the database."""
        # TODO: Implement database saving functionality
        raise NotImplementedError("Database saving functionality not implemented yet") 

    @classmethod
    def load(cls, candidate_id: int) -> 'Candidate':
        """
        Load a candidate from the database.
        
        Args:
            candidate_id: The ID of the candidate to load
            
        Returns:
            Candidate: The loaded candidate instance
            
        Raises:
            NotImplementedError: If database loading is not implemented
        """
        raise NotImplementedError("Database loading functionality not implemented yet") 