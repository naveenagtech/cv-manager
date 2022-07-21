import re

SKILLS = [
    'machine learning',
    'data science',
    'python',
    'Creative design',
    'word',
    'excel',
    'Strong decision maker',
    'English',
    'web developer',
    'Innovative',
    'html',
    'Service-focused',
    'Complex problem solver',
    'css',
    'Project management'
]

def find_skills(text):
    """
        A function to find Skills from the text using Regular Expression
        created by: Sumit Saurav
    """
    skills = []
    for i in skills:
        pattern = re.compile(i)
        if bool(re.search(pattern, text.lower())):
            skills.append(i)
    return skills



def find_email(text):
    """
        A function to find Email from the text using Regular Expression
        created by: Sumit Saurav
    """
    email_=r'[A-Za-z0-9]+[\._]?[a-z0-9]+[@]\w+[-]?\w+[.]\w{2,3}'
    email=re.findall(email_,text)
    return email[0]



def find_phone(text):
    """
        A function to find phone number from the text using Regular Expression
        created by: Sumit Saurav
    """
    phn_ = r'[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}'
    phone=re.findall(phone,text)
    return phone[0]


def find_name(text):
    name = "Name"
    return name