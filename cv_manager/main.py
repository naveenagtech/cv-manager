import sqlite3
import os
from cv_manager.process_doc import get_data_from_doc
from db_manager.query import CREATE_TABLE_QUERY
from cv_manager.process_pdf import get_data_from_pdf
UPLOAD_DIR = os.path.join(os.getcwd(), "uploads")




def save_data(data):
    """
    Save the data in DB using the db functions
    """
    conn = sqlite3.connect("<database_name>")
    cursor = conn.cursor()
    cursor.execute(CREATE_TABLE_QUERY)
    conn.commit()
    conn.close()
    print("Save Detail")
    pass

def extract_data_from_file():
    all_files = os.listdir(UPLOAD_DIR)
    for file in all_files:
        if file.lower().endswith(".docx"):
            data = get_data_from_doc(os.path.join(UPLOAD_DIR, file))
        elif file.lower().endswith(".pdf"):
            # print("File")
            # call pdf parser
            data = get_data_from_pdf(os.path.join(UPLOAD_DIR, file))
        elif file.lower().endswith(".jpg"):
            # call image parser
            data = None
    return data

def process_cv():
    # print("processing")
    extract_data_from_file()