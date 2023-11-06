import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

DB = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    db=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASS")
)