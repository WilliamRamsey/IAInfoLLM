from Job import Job
from typing import Optional

query_jobs_declaration = {
    "name": "query_jobs",
    "description": "Returns a list of string representations job listings that meet the minimum salary and location.",
    "parameters": {
        "type": "object",
        "properties": {
            "minimum_salary": {
                "type": "integer",
                "description": "The absolute minimum salary a candidate is willing to work for."
            },
            "location": {
                "type": "string",
                "description": "The city where a candidate wants to find their new job."
            }
        },
        "required": ["minimum_salary", "location"]
    }
}

def query_jobs(minimum_salary: int, location: str) -> str:
    print(f"Gemini called with {minimum_salary}, {location}")
    all_jobs = Job.jobs_from_file()
    matched_jobs = ""
    for job in all_jobs:
        if job.get_salary() > minimum_salary and job.get_location() == location:
            matched_jobs += f"{str(job)}\n"
    return matched_jobs



