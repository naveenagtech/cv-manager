import sqlite3
import query
def create_user(id, name, email, phone_number,skills,file_path):
        """
        Create a function to insert data extracted from CV to DB

        Created By: priyanshi.srivastva@ag-technologies.com
        """
        INSERT_USER_QUERY = """INSERT INTO <Table_Name> (id, name, email, phone_number,skills,file_path) VALUES({},{},{},{},{},{});"""
        conn = sqlite3.connect("<Database name>")
        cursor = conn.cursor()
        cursor.execute(INSERT_USER_QUERY.format(id, name, email, phone_number,skills,file_path))
        conn.commit()
        conn.close()