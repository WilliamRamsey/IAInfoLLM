from Job import Job

# all declarations are for candidate agent

# Job class method
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

# JobDesires instance method
set_candidate_ideal_salary_declaration = {
    "name": "set_candidate_ideal_salary",
    "description": "Saves the candidate's desired salary for use in future prompt context.",
    "parameters": {
        "type": "object",
        "properties": {
            "ideal_salary": {
                "type": "integer",
                "description": "The salary a candidate ideally wants to make in their new role."
            }
        },
        "required": ["ideal_salary"]
    }
}

set_candidate_minimum_salary_declaration = {
    "name": "set_candidate_minimum_salary",
    "description": "Saves the candidate's minimum acceptable salary for use in future prompt context.",
    "parameters": {
        "type": "object",
        "properties": {
            "minimum_salary": {
                "type": "integer",
                "description": "The absolute minimum salary a candidate is willing to accept."
            }
        },
        "required": ["minimum_salary"]
    }
}

set_candidate_location_declaration = {
    "name": "set_candidate_location",
    "description": "Saves the candidate's preferred job location for use in future prompt context.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city or region where the candidate wants to work."
            }
        },
        "required": ["location"]
    }
}

set_candidate_position_declaration = {
    "name": "set_candidate_position",
    "description": "Saves the candidate's desired job position for use in future prompt context.",
    "parameters": {
        "type": "object",
        "properties": {
            "position": {
                "type": "string",
                "description": "The job title or position the candidate wants."
            }
        },
        "required": ["position"]
    }
}

set_candidate_job_description_declaration = {
    "name": "set_candidate_job_description",
    "description": "Saves the candidate's desired job description for use in future prompt context.",
    "parameters": {
        "type": "object",
        "properties": {
            "description": {
                "type": "string",
                "description": "The job description the candidate is looking for."
            }
        },
        "required": ["description"]
    }
}

set_candidate_company_culture_declaration = {
    "name": "set_candidate_company_culture",
    "description": "Saves the candidate's preferred company culture for use in future prompt context.",
    "parameters": {
        "type": "object",
        "properties": {
            "company_culture": {
                "type": "string",
                "description": "The type of company culture the candidate prefers."
            }
        },
        "required": ["company_culture"]
    }
}

set_candidate_responsibilities_declaration = {
    "name": "set_candidate_responsibilities",
    "description": "Saves the candidate's preferred job responsibilities for use in future prompt context.",
    "parameters": {
        "type": "object",
        "properties": {
            "responsibilities": {
                "type": "string",
                "description": "The responsibilities the candidate wants in a job."
            }
        },
        "required": ["responsibilities"]
    }
}

set_candidate_work_experience_declaration = {
    "name": "set_candidate_work_experience",
    "description": "Saves the candidate's work experience for use in future prompt context.",
    "parameters": {
        "type": "object",
        "properties": {
            "work_experience": {
                "type": "array",
                "items": {"type": "string"},
                "description": "A list of the candidate's work experiences."
            }
        },
        "required": ["work_experience"]
    }
}

set_candidate_education_declaration = {
    "name": "set_candidate_education",
    "description": "Saves the candidate's educational qualifications for use in future prompt context.",
    "parameters": {
        "type": "object",
        "properties": {
            "education": {
                "type": "array",
                "items": {"type": "string"},
                "description": "A list of the candidate's educational qualifications."
            }
        },
        "required": ["education"]
    }
}

set_candidate_skills_declaration = {
    "name": "set_candidate_skills",
    "description": "Saves the candidate's skills for use in future prompt context.",
    "parameters": {
        "type": "object",
        "properties": {
            "skills": {
                "type": "array",
                "items": {"type": "string"},
                "description": "A list of the candidate's technical and soft skills."
            }
        },
        "required": ["skills"]
    }
}





