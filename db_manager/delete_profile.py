import sqlite3

from db_manager.query import DELETE_USER_QUERY


def delete_user(ID):

 
    """
    Create a function to delete row from the user table based on the ID
    
    Created By: kajal.rituraj@ag-technologies.com
    """

    conn = sqlite3.connect("<databasename>")
    cursor = conn.cursor()
    cursor.execute(DELETE_USER_QUERY + str(ID))
    conn.commit() 
    conn.close()