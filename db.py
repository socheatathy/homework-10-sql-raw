import os
from dotenv import load_dotenv
import mysql.connector
from datetime import datetime

load_dotenv()

DB = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    db=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASS"),
    port=os.getenv("DB_PORT")
)

cursor = DB.cursor()

'''
Query all employee records from the employee table
And query employee with condition, emp_num > 101
'''

# cursor.execute("SELECT * FROM employee")
# employees = cursor.fetchall()
# print (employees)

# for employee in employees:
#     print(employee[0], employee[1], employee[2], employee[3], employee[4].strftime('%d-%B-%Y'))

# date time conversion format
# https://www.w3schools.com/python/python_datetime.asp#:~:text=A%20reference%20of%20all%20the%20legal%20format%20codes%3A

# cursor.execute("SELECT * FROM employee WHERE emp_num > 101")
# employees_condition = cursor.fetchall()

# for employee in employees_condition:
#     print(employee[0], employee[1], employee[2], employee[3], employee[4].strftime('%d-%B-%Y'))

'''
Join employee with job and select emp_num, emp_lname, emp_fname, emp_initial, emp_hiredate, job_description
'''

# cursor.execute("SELECT * FROM employee INNER JOIN job ON employee.job_code = job.job_code")
# employees = cursor.fetchall()
# for employee in employees:
#     print(employee[0], employee[1], employee[2], employee[3], employee[4].strftime('%d-%B-%Y'), employee[9])

# OR

# cursor.execute('''SELECT 
#                em.emp_num, em.emp_lname, em.emp_fname, em.emp_initial, em.emp_hiredate, job.job_description  
#                FROM employee as em INNER JOIN job ON em.job_code = job.job_code''')

# employees = cursor.fetchall()
# for employee in employees:
#     print(employee[0], employee[1], employee[2], employee[3], employee[4].strftime('%d-%B-%Y'), employee[5])

'''
Insert new employee record, emp_num = 999, emp_lname = Doe, emp_fname = John, emp_initial = D, emp_hiredate = current date
'''
# today = datetime.now()
# sql = "INSERT INTO employee (emp_num, emp_lname, emp_fname, emp_inital, emp_hiredate) VALUES (%s, %s, %s, %s, %s)"
# value = (999, "doe", "jhn", "D", today)
# cursor.execute(sql, value)
# DB.commit()

'''
Update employee record, job_code = 510 where emp_num = 999
'''



'''
Delete employee record, emp_num = 999
'''



'''
Query assigment where assign_date is larger than 2010-01-01
'''



# 1. question 1

# today = datetime.now()
# sql="INSERT INTO employee (emp_num, emp_lname, emp_fname, emp_initial, emp_hiredate, job_code) VALUES(%s, %s, %s, %s, %s, %s)"
# value= (168, "Doe", "John", "JD", today, 500)

# cursor.execute(sql, value)

# DB.commit()

# print(cursor.rowcount, "record inserted.") 

# 2. question 2
# sql = """
#     SELECT 
#         E.EMP_NUM, 
#         E.EMP_FNAME, 
#         E.EMP_LNAME, 
#         E.EMP_INITIAL, 
#         J.JOB_DESCRIPTION, 
#         J.JOB_CHG_HOUR, 
#         E.EMP_HIREDATE
#     FROM 
#         employee AS E 
#     JOIN 
#         job AS J ON E.JOB_CODE = J.JOB_CODE 
#     WHERE 
#         E.EMP_NUM = 168;
# """
# cursor.execute(sql)

# result = cursor.fetchone()

# print("Employee ID:", result[0],
#       "\nFirst Name:", result[1], 
#       "\nLast Name:", result[2], 
#       "\nInitial:", result[3],
#       "\nJob Description:", result[4],
#       "\nCharge per Hour:", result[5],
#       "\nHire Date:", result[6])

# 3. question 3

# update_sql = """
#     UPDATE employee
#     SET job_code = (SELECT job_code FROM job WHERE job_description = 'Database Designer')
#     WHERE emp_num = 168;
# """

# cursor.execute(update_sql)

# DB.commit()

# print(cursor.rowcount, "Successfully upadted.") 

# 4. question 4

# sql = """
#     SELECT
#         P.PROJ_NUM,
#         P.PROJ_NAME,
#         E.EMP_FNAME,
#         E.EMP_LNAME
#     FROM
#         project AS P
#     JOIN
#         `assignment` AS A ON P.PROJ_NUM = A.PROJ_NUM
#     JOIN
#         employee AS E ON A.EMP_NUM = E.EMP_NUM
#     JOIN
#         job AS J ON E.JOB_CODE = J.JOB_CODE
#     WHERE
#         J.JOB_DESCRIPTION = 'Programmer';
# """
# cursor.execute(sql)
# result = cursor.fetchall()
# print(result)


# 5. question 5

delete_sql = """
    DELETE FROM employee 
    WHERE EMP_NUM = 168;
"""
cursor.execute(delete_sql)

DB.commit()

print(cursor.rowcount, "Successfully deleted.")