import os
from cv_manager.process_doc import get_data_from_doc
from cv_manager.process_pdf import get_data_from_pdf
UPLOAD_DIR = os.path.join(os.getcwd(), "uploads")

def save_data(data):
    """
    Save the data in DB using the db functions
    """
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