from pyresparser import ResumeParser

def final_parser(file_path):
    data = ResumeParser(file_path).get_extracted_data()
    print(data)
    return data


