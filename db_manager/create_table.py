import sqlite3
from query import CREATE_TABLE_QS

def create_table():
    conn = sqlite3.connect("new_table.db")
    cursor = conn.cursor()
    cursor.execute(CREATE_TABLE_QS)
    conn.close()
    print("Created Employee Table")