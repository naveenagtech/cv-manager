import email
import sqlite3
from unicodedata import name

from query import FETCH_USER_QUERY

def fetch_user():
    """
    Create a function to fetch users fro DB

    Created By: lopamudra.sahoo@ag-technologies.com
    """
     
    conn = sqlite3.connect("<databasename>")
    cursor = conn.cursor()
    cursor.execute(FETCH_USER_QUERY + str(id,name,email))
    conn.commit() 
    conn.close()