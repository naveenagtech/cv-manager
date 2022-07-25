import os
import shutil
from datetime import datetime
from cv_manager.process_doc import get_data_from_doc
# from cv_manager.final_pyparser import final_parser
from db_manager.create_profile import create_user
from cv_manager.process_pdf import get_data_from_pdf


UPLOAD_DIR = os.path.join(os.getcwd(), "uploads")
PROCESSED_DIR = os.path.join(os.getcwd(), "uploads", "processed")


def handle_processed_file(upload_file_path, file):

    today = datetime.strftime(datetime.now().date(), "%Y-%d-%m")
    processed_file_path = os.path.join(PROCESSED_DIR, today)
    os.makedirs(processed_file_path, exist_ok=True)
    shutil.move(upload_file_path, os.path.join(processed_file_path, file))

def ocr_reader():

    """
    1 - Fech all data from user table where system_validated = False
    2 - Get the file_path of the row where system_validated = False and save it to file_path = /processed/2022-23-07/Ajay_Choudhary_Frontend_Resume.pdf
    3 - convert the above file to image 
    4 - read the text from the image
    5 - extract the data from the text
    6 - save the image with file_path.<img>

    """
    pass

def extract_data_from_file():
    all_files = os.listdir(UPLOAD_DIR)
    for file in all_files:
        upload_file_path = os.path.join(UPLOAD_DIR, file)

        if file.lower().endswith(".docx") or file.lower().endswith(".doc"):
            data, text = get_data_from_doc(upload_file_path, file)
            create_user(data)
        elif file.lower().endswith(".pdf"):
            data, text = get_data_from_pdf(upload_file_path, file)
            create_user(data)
        elif file.lower().endswith(".jpg"):
            # call image parser
            data = None
        else:
            data = None
        
        if data is not None:
            handle_processed_file(upload_file_path, file)
    return data


def process_cv():
    extract_data_from_file()
