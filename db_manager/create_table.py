import sqlite3
from db_manager.query import (
    CREATE_USER_TABLE_QUERY,
    CREATE_SKILLS_CATEGORY_TABLE,
    CREATE_SKILLS_TABLE,
    INSERT_CATEGORY_QUERY
)
from db_manager import DB

def create_user_table():
    """
    This function will create a database for the project is the db is not there already
    Created By: nirupama.sahoo@ag-technologies.com 
    """
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute(CREATE_USER_TABLE_QUERY)
    conn.close()


def create_skill_table():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute(CREATE_SKILLS_CATEGORY_TABLE)
    conn.close()

def create_category_table():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute(CREATE_SKILLS_TABLE)
    conn.close()

def create_categories():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    names = [
        "BACKEND",
        "FRONTEND",
        "MARKETING",
        "DESIGNER",
        "DATA_SCIENCE",
        "FULLSTACK",
        "ACCOUNTANT"
    ]
    cursor.execute("SELECT * FROM CATEGORY")
    data = cursor.fetchall()
    if len(data) == 0:
        for i in names:
            q = INSERT_CATEGORY_QUERY%{"name": i}
            cursor.execute(q)
        conn.commit()
    conn.close()