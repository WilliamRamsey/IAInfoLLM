```mermaid
classDiagram
    class Job {
        -int __job_count$
        -int __id
        -string __title
        -string __company
        -int __salary
        -string __description
        +{static} jobs_from_file() list~Job~
        +__init__(title: str, company: str, salary: int?, description: str?, id: int?)
        +set_salary(new_salary: int) void
        +update_description(new_description: str) void
        +save() void
        +__str__() string
    }

    note for Job "Represents a job listing\nDo not use commas in any text fields\ntitle, company, salary, description"
```

# Job Class Documentation

## Class Description
The `Job` class represents a job listing with attributes for title, company, salary, and description. It includes functionality to load jobs from a CSV file and save new job listings.

## Attributes
- `__job_count` (static): Counter for total number of jobs
- `__id`: Unique identifier for the job
- `__title`: Job title
- `__company`: Company name
- `__salary`: Optional salary amount
- `__description`: Optional job description

## Methods
- `jobs_from_file()`: Static method that loads jobs from Jobs.csv
- `__init__()`: Constructor that initializes a new job listing
- `set_salary()`: Updates the job's salary
- `update_description()`: Updates the job's description
- `save()`: Saves the job to Jobs.csv
- `__str__()`: Returns a string representation of the job