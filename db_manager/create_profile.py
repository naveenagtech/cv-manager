import sqlite3
import query
def create_user():
        """
        Create a function to insert data extracted from CV to DB

        Created By: priyanshi.srivastva@ag-technologies.com
        """
        CREATE_TABLE_QUERY = """
         CREATE TABLE IF NOT EXISTS Detail
        (
             id INT PRIMARY KEY NOT NULL,
            name VARCHAR(255),
            email VARCHAR(255),
            phone_number INT ,
            skills VARCHAR(255),
            file_path VARCHAR(255)
        );
    """
        conn = sqlite3.connect("new_db.db")
        cursor = conn.cursor()
        cursor.execute(CREATE_TABLE_QUERY)
        conn.commit()
        conn.close()
        print("Created Detail Table")
        pass