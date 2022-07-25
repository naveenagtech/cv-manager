import sqlite3
from db_manager.query import DELETE_USER_QUERY
from db_manager import DB


def delete_user(id):
    """
    To delete a row from the user table based on the primary Key
    
    Created By: kajal.rituraj@ag-technologies.com
    """

    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    data = {"id": id}
    q = DELETE_USER_QUERY%data
    print(q)
    cursor.execute(q)
    conn.commit() 
    conn.close()