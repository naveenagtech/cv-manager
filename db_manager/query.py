"""
Write query to create a table to database to store below information
id
name
email
phone_number
skills
file_path
nirupama.sahoo@ag-technologies.com
"""
CREATE_TABLE_QUERY = "CREATE TABLE IF NOT EXISTS user"

"""
Write SQL query to Insert data in the above table
nirupama.sahoo@ag-technologies.com
"""
INSERT_USER_QUERY = """INSERT INTO <Table_Name> (id, name, email, phone_number,skills,file_path) VALUES({},{},{},{},{},{});"""

"""
Write SQL query to Fetch data from the above table
priyanshi.srivastva@ag-technologies.com
"""
FETCH_USER_QUERY = ""

"""
Write SQL query to delete data from the above table based on the ID
kajal.rituraj@ag-technologies.com
"""
DELETE_USER_QUERY="DELETE FROM user WHERE userId = "