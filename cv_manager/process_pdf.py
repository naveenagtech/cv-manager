"""
Import the common helper function like find_skills, find_email etc
"""
from cgitb import text
from urllib import response
import PyPDF2
import re
import glob

from cv_manager.common import find_email, find_name, find_phone, find_skills

def get_text_from_file(file_path):
    """
        Crate a function to extract text from the PDF file
        this function will take file path as a param and will return text data
        file_path: Path of the doc file
        Created By: Nitesh
    """
    content=open(file_path,"rb")
    object=PyPDF2.PdfReader(content)
    pages=object.getNumPages()
    text=""
    for page in range(pages):
        page = object.getPage(page)
        text_data=page.extract_text()
        text+=text_data
    return text
  
    

def get_data_from_pdf(file_path):
    """
        Create a function which will use common helper function to extract data from the text content
        and return the response in below format
        text_content: Text data extracted from PDF file with the help of get_text_from_file function
        {
            "name": "Name",
            "email": "Email",
            "phone": "Phone",
            "skills": ["skill1", "skill2"]
        }
        Created By:nitesh.chauhan@ag-technologies.com
    """
    text=get_text_from_file(file_path)
    response={
            "name": find_name(text),
            "email": find_email(text),
            "phone": find_phone(text),
            "skills":find_skills(text)
        }
    print(response)
    return response

