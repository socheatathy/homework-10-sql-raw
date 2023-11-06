from db import DB

class Job:
    def __init__(self, job_code, job_description, job_chg_hour, job_last_update):
        self.job_code = job_code
        self.job_description = job_description
        self.job_chg_hour = job_chg_hour
        self.job_last_update = job_last_update

    def get_job(self, job_code):
        ...
    
    def add_job(self, job_code, job_description, job_chg_hour):
        ...
    
    def remove_job(self, job_code):
        ...
    
    def update_job(self, job_code, job_description, job_chg_hour):
        ...