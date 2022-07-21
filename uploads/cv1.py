import docx
import docx2txt
import re
WED_DEV_SKILLS = [
    'Zend',
    'Codeigniter',
    'Symfony',
    'JavaScript',
    'HTML5',
    'PHP OOP',
    'SQL',
    'MySQL'
]
email=re.compile(r'[a-zA-Z0-9]+[a-zA-Z0-9]@+[a-zA-Z0-9-\.]+[a-zA-Z0-9]')
phone_num=re.compile(r'[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}')
linkdin=re.compile(r'(http|ftp|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])')

def my_text(file_path):
    file_content=open(file_path)
    return file_content

def find_skills(my_text):
    skills = []
    for i in WED_DEV_SKILLS:
        pattern = re.compile(i)
        if bool(re.search(pattern, my_text.lower())):
            skills.append(i)
    return skills

my_text=docx2txt.process("C:\\Users\\lopamudra.sahoo\\Desktop\\files\\cv.docx")
phone_num=re.findall(phone_num,my_text)
email=re.findall(email,my_text)
linkdin=re.findall(linkdin,my_text)
skills = find_skills(my_text)
print(phone_num)
print(email)
print(linkdin)
print(skills)