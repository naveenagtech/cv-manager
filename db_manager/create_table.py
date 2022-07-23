import sqlite3
from query import CREATE_TABLE_QS



def create_table():

    """
    Create a function to create table using the create table query

    Created By: nirupama.sahoo@ag-technologies.com 
    """


    conn = sqlite3.connect("new_table.db")
    cursor = conn.cursor()
    cursor.execute(CREATE_TABLE_QS)
    conn.close()
    print("Created Employee Table")
    pass