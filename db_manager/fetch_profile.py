import sqlite3
from db_manager.query import FETCH_USER_QUERY
from db_manager import DB

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]

def fetch_user():
    """
    This function will fetch usr data from the table

    Created By: lopamudra.sahoo@ag-technologies.com
    """
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute(FETCH_USER_QUERY)
    data = dictfetchall(cursor)
    conn.commit() 
    conn.close()
    
    return data