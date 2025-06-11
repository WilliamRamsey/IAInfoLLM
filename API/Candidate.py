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
    # Qualititive attributes
    ideal_salary: Optional[int] = None
    minimum_salary: Optional[int] = None
    location: Optional[str] = None
    position: Optional[str] = None
    job_description: Optional[str] = None
    
    # Semantic attributes
    company_culture: Optional[str] = None
    responsibilities: Optional[str] = None
    
    def set_ideal_salary(self, salary: int):
        self.ideal_salary = salary

    def set_minimum_salary(self, salary: int):
        self.minimum_salary = salary

    def set_location(self, location: str):
        self.location = location

    def set_position(self, position: str):
        self.position = position

    def set_job_description(self, description: str):
        self.job_description = description

    def set_company_culture(self, culture: str):
        self.company_culture = culture

    def set_responsibilities(self, responsibilities: str):
        self.responsibilities = responsibilities
    
    def __str__(self):
        return f"Ideal salary: {self.ideal_salary}, Minimum salary: {self.minimum_salary} location: {self.location}, position: {self.position}, description: {self.job_description}, company culture: {self.company_culture}, responsibilities: {self.responsibilities}"

@dataclass
class Qualifications:
    """
    Candidate's work experience and qualifications
    """
    work_experience: Optional[List[str]] = None  # List of work experiences with company, role, duration, etc.
    education: Optional[List[str]] = None # List of educational qualifications
    skills: Optional[List[str]] = None # List of technical and soft skills

    def set_work_experience(self, work_experience: list[str]):
        self.work_experience = work_experience

    def set_education(self, education: list[str]):
        self.education = education

    def set_skills(self, skills: list[str]):
        self.skills = skills

    def __str__(self):
        return f"work experience: {self.work_experience}, education: {self.education}, skills: {self.skills}"

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
        
    # --- JobDesires setters ---
    def set_ideal_salary(self, ideal_salary: int):
        self.__job_desires.set_ideal_salary(ideal_salary)

    def set_minimum_salary(self, minimum_salary: int):
        self.__job_desires.set_minimum_salary(minimum_salary)

    def set_location(self, location: str):
        self.__job_desires.set_location(location)

    def set_position(self, position: str):
        self.__job_desires.set_position(position)

    def set_job_description(self, description: str):
        self.__job_desires.set_job_description(description)

    def set_company_culture(self, culture: str):
        self.__job_desires.set_company_culture(culture)

    def set_responsibilities(self, responsibilities: str):
        self.__job_desires.set_responsibilities(responsibilities)

    # --- Qualifications setters ---
    def set_work_experience(self, work_experience: list[str]):
        self.__qualifications.set_work_experience(work_experience)

    def set_education(self, education: list[str]):
        self.__qualifications.set_education(education)

    def set_skills(self, skills: list[str]):
        self.__qualifications.set_skills(skills)

    def __str__(self):
        return f"{self.__name} wants a job with the following information:\n{str(self.__job_desires)}\nThe candidate has the following qualifications: {str(self.__qualifications)}"

