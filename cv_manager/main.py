import os
from cv_manager.process_doc import get_data_from_doc
UPLOAD_DIR = os.path.join(os.getcwd(), "uploads")

def extract_data_from_file():
    all_files = os.listdir(UPLOAD_DIR)
    for file in all_files:
        if file.lower().endswith(".docx"):
            data = get_data_from_doc(os.path.join(UPLOAD_DIR, file))
        elif file.lower().endswith(".pdf"):
            # call pdf parser
            pass
    return data

def process_cv():
    print("processing")