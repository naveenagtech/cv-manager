import sqlite3
from db_manager.query import INSERT_USER_QUERY
from db_manager import DB
from cv_manager.common import find_category

def create_user(data):
    """
    This function will take data as argument and insert the data in DB
    Created By: priyanshi.srivastva@ag-technologies.com
    """
    try:
        conn = sqlite3.connect(DB)
        cursor = conn.cursor()
        q = INSERT_USER_QUERY%data
        cursor.execute(q)
        conn.commit()
        find_category(cursor.lastrowid)
        conn.close()
    except Exception as e:
        print(q)
        print(e)