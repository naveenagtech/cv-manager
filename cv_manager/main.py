from cgitb import text
import os
import shutil
from datetime import datetime
import sqlite3
from cv_manager.converter import doc_pdf_to_img
from cv_manager.process_doc import get_data_from_doc
from cv_manager.process_img import get_ocr_data, get_text_from_img
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

    FETCH_NONE_SYSTEM_VALIDATED_DATA = "SELECT * FROM user where system_validated = 0;"

    # Fetching data
    connection = sqlite3.connect('sqlite.db')
    cursor = connection.cursor()
    cursor.execute(FETCH_NONE_SYSTEM_VALIDATED_DATA)
    all_data = cursor.fetchall()

    list_of_file_path = []  
    for data in all_data:
        list_of_file_path.append(data[7])
    connection.close()


    # Extracting Data from Images using OCR reader
    for file_path in list_of_file_path:
        print("hello" + file_path)
        # If File is DOC / DOCX / PDF then convert it to Image first then text is extracted
        if file_path.endswith(".docx") or file_path.endswith(".doc") or file_path.endswith(".pdf"):
            images_containing_folder = doc_pdf_to_img(file_path)
        
            images_in_folder = os.listdir(images_containing_folder)
            text_content = ""

            for images in images_in_folder:
                text_content = text_content + get_text_from_img(images_containing_folder + "\\" + images) + " "            
        else:
            text_content = get_text_from_img(file_path)
            

        extracted_data =  get_ocr_data(text_content)
        print(extracted_data)

        # Next step is to compare with original extracted data nad updating it to database
        # Go to compare and update file for the next operation


def ocr_reader_for_doc_pdf(name):
    # Fetching file_path
    connection = sqlite3.connect('sqlite.db')
    cursor = connection.cursor()
    cursor.execute("SELECT system_validated, file_path FROM user where name = '" + name + "';")
    data = cursor.fetchone()
    file_path = data[1]
    connection.close()

    image_storage_path = doc_pdf_to_img(file_path)
    print(image_storage_path)


def extract_data_from_file():
    all_files = os.listdir(UPLOAD_DIR)
    for file in all_files:
        upload_file_path = os.path.join(UPLOAD_DIR, file)

        if file.lower().endswith(".docx") or file.lower().endswith(".doc"):
            data, text = get_data_from_doc(upload_file_path, file)
            create_user(data)

            ocr_data = ocr_reader_for_doc_pdf(data.get("name"))
        elif file.lower().endswith(".pdf"):
            data, text = get_data_from_pdf(upload_file_path, file)
            create_user(data)
        elif file.lower().endswith(".jpg"):
            # call image parser 
            data = get_ocr_data(upload_file_path, file)
            create_user(data)
            print(data)
            data = None
        else:
            data = None
        
        if data is not None:
            handle_processed_file(upload_file_path, file)
    return data


def process_cv():
    extract_data_from_file()
