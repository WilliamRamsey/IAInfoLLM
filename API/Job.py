from __future__ import annotations

"""
# Represents a job listing
## Do not use commas in any text feilds
title, company, salary, description
"""
class Job:
    __job_count = 0
    # Works like a lot like a Java static method, but respects inheritence
    # Very boldly assuemes there are no commas in titles or descriptions
    @classmethod
    def jobs_from_file(cls) -> list['Job']:
        with open("Jobs.csv", "r") as f:
            lines = f.readlines()
        f.close()
        Job.__job_count = len(lines)

        # cls() is the constructor for the job class
        jobs = []
        for job_string in lines:
            # assumes correct formatting
            job_attributes = job_string.split(", ")
            jobs.append(
            cls(
                title = str(job_attributes[1]),
                company = str(job_attributes[2]),
                salary = int(job_attributes[3]),
                description = str(job_attributes[4],
                                  )
                )
            )
        return jobs

    def __init__(self, title: str, company: str, salary: int | None = None, description: str | None = None, id: int | None = None) -> None:
        if id == None:
            with open("Jobs.csv", "r") as f:
                lines = f.readlines()
            f.close()
            Job.__job_count = len(lines) + 1

            self.__id = Job.__job_count
        else:
            self._id = id
        
        self.__title = title
        self.__company = company
        self.__salary = salary
        self.__description = description

    def set_salary(self, new_salary: int):
        self.__salary = new_salary

    def update_description(self, new_description: str):
        self.__description = new_description

    def save(self):
        with open("Jobs.csv", "a") as f:
            f.write(f"{self.__id}, {self.__title}, {self.__company}, {self.__salary}, {self.__description}\n")
    
    def __str__(self):
        job_info = f"Job (No. {self.__id}): {self.__title} at {self.__company}"
        if self.__salary:
            job_info += f", Salary: {self.__salary}"
        if self.__description:
            job_info += f", Description: {self.__description}"
        return job_info
