import sqlite3
from db_manager.query import (
    CREATE_USER_TABLE_QUERY,
    CREATE_SKILLS_CATEGORY_TABLE,
    CREATE_SKILLS_TABLE,
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