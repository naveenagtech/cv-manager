import sqlite3
from db_manager import DB

def update_user(data):

    conn = sqlite3.connect(DB)
    curr = conn.cursor()

    query = "UPDATE user set "
    
    if "user_validated" in data:
        data.update({
            "user_validated": data['user_validated']
        })
    else:
        data.update({
            "user_validated": False
        })
    for key, value in data.items():
        if key != "id":
            query += "{}='{}',".format(key, value)
    
    query = query[:-1]
    query += " where id = {}".format(data['id'])
    
    curr.execute(query)
    conn.commit()
    conn.close()
    