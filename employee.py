from db import DB

class Employee:
    def __init__(self, emp_num, emp_lname, emp_fname, **kwarg) -> None:
        self.emp_num = emp_num
        self.emp_lname = emp_lname
        self.emp_fname = emp_fname
        self.emp_initial = kwarg.get('emp_initial', None)

    @classmethod
    def get_employee(cls, emp_num):
        ...
    
    def register(self, emp_num, emp_lname, emp_fname, **kwarg):
        ...
    

    def remove(self, emp_num):
        ...
    
    def update(self, emp_num, emp_lname, emp_fname, **kwarg):
        ...
