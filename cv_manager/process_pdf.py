import PyPDF2
import json
from datetime import datetime
from cv_manager.common import find_email, find_name, find_phone, find_skills

today = datetime.strftime(datetime.now().date(), "%Y-%d-%m")

def get_text_from_file(file_path):
    """
        Crate a function to extract text from the PDF file
        this function will take file path as a param and will return text data
        file_path: Path of the doc file
        Created By: Nitesh
    """
    try:
        content=open(file_path,"rb")
        object=PyPDF2.PdfReader(content)
        pages=object.getNumPages()
        text=""
        for page in range(pages):
            page = object.getPage(page)
            text_data=page.extract_text()
            text+=text_data
        content.close()
        return text
    except Exception as e:
        print("Error: ", e)
  
    

def get_data_from_pdf(file_path, file_name):
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
    try:
        text=get_text_from_file(file_path)
        response={
            "name": find_name(text),
            "email": find_email(text),
            "phone": find_phone(text),
            "skills": json.dumps(find_skills(text))
        }
        if all([list(response.values())]):
            response.update({"system_validated": True})
        else:
            response.update({"system_validated": False})
        
        response.update({
            "file_path": "/processed/{}/{}".format(today, file_name)
        })
        return response, text

    except Exception as e:
        print("Error: ", e)
        return None, None
