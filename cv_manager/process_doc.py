import docx2txt
from datetime import datetime
from cv_manager.common import find_email, find_name, find_phone, find_skills

today = datetime.strftime(datetime.now().date(), "%Y-%d-%m")

def get_text_from_file(file_path):
    """
        This function will take file path as a param and will return text data
        file_path: Path of the doc file
        Created by: Naveen Singh
    """
    try:
        text_content = docx2txt.process(file_path)
        return text_content
    except Exception as e:
        print(e)


    


def get_data_from_doc(file_path, file_name):
    """
        Returns the response in below format
        text_content: Text data extracted from doc file with the help of get_text_from_file function
        {
            "name": "Name",
            "email": "Email",
            "phone": "Phone",
            "skills": ["skill1", "skill2"]
        }

        Created by: Naveen Singh
    """
    try:
        text_content = get_text_from_file(file_path)

        extracted_data = {
            "name": find_name(text_content),
            "email": find_email(text_content),
            "phone": find_phone(text_content),
            "skills": find_skills(text_content),
        }
        if all([list(extracted_data.values())]):
            extracted_data.update({"system_validated": True})
        else:
            extracted_data.update({"system_validated": False})
        
        extracted_data.update({
            "file_path": "/processed/{}/{}".format(today, file_name)
        })
        return extracted_data, text_content
    except Exception as e:
        print(e)
        return None, None