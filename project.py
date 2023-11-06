from db import DB

class Project:
    def __init__(self, proj_num, proj_name, proj_value, proj_balance, manager_num):
        self.proj_num = proj_num
        self.proj_name = proj_name
        self.proj_value = proj_value
        self.proj_balance = proj_balance
        self.manager_num = manager_num

    def get_project(self, proj_num):
        ...
    
    def add_manager(self, proj_num, manager_num):
        ...
    
    def remove_manager(self, proj_num):
        ...
    
    def update_project(self, proj_num, proj_name, proj_value, proj_balance):
        ...