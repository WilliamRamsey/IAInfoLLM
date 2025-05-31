from __future__ import annotations
from typing import Optional, List, Dict
from dataclasses import dataclass
from datetime import datetime
from Job import Job

@dataclass
class JobDesires:
    """
    Standard and semantic job preferences for a candidate.
    Yes this is redundant with the Job class, 
    """
    # Standard query attributes
    salary: Optional[int] = None
    location: Optional[str] = None
    position: Optional[str] = None
    description: Optional[str] = None
    
    # Semantic attributes
    company_culture: Optional[str] = None
    responsibilities: Optional[str] = None

    def __str__(self):
        return f"salary: {self.salary}, location: {self.location}, position: {self.position}, description: {self.description}, company culture: {self.company_culture}, responsibilities: {self.responsibilities}"
    
@dataclass
class Qualifications:
    """
    Candidate's work experience and qualifications
    """
    work_experience: Optional[List[str]] = None  # List of work experiences with company, role, duration, etc.
    education: Optional[List[str]] = None # List of educational qualifications
    skills: Optional[List[str]] = None # List of technical and soft skills

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
        job_desires: Optional[JobDesires] = None,
        qualifications: Optional[Qualifications] = None,
        id: Optional[int] = None
    ) -> None:
        """
        Initialize a new candidate with their basic information and preferences.
        
        Args:
            name: Candidate's full name
            email: Candidate's email address
            job_desires: Optional job preferences
            qualifications: Optional work experience and qualifications
            soft_info: Optional text embedding of soft information
            id: Optional unique identifier
        """
        
        # ID inc.
        if id is None:
            Candidate.__candidate_count += 1
            self.__id = Candidate.__candidate_count
        else:
            self.__id = id

        self.__name = name
        self.__email = email
        self.__job_desires = job_desires or JobDesires()
        self.__qualifications = qualifications or Qualifications([], [], [])
        self.__offers: List[Job] = []  # List of job offers received
        
    def __str__(self):
        return f"{self.__name} wants a job with the following information:\n{str(self.__job_desires)}"

