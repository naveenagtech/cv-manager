import re
import spacy
import subprocess as sp
try:
    import en_core_web_lg
except:
    sp.Popen(["python -m spacy download en_core_web_lg"])

nlp = spacy.load("en_core_web_lg")

SKILLS = [
    "machine learning",
    "data science",
    "python",
    "Creative design",
    "word",
    "excel",
    "Strong decision maker",
    "English",
    "web developer",
    "Innovative",
    "html",
    "Service-focused",
    "Complex problem solver",
    "css",
    "Project management",
]


def find_skills(text):
    """
    A function to find Skills from the text using Regular Expression
    created by: Sumit Saurav
    """
    skills = []
    for i in skills:
        pattern = re.compile(i.lower())
        if bool(re.search(pattern, text.lower())):
            skills.append(i)
    return skills


def find_email(text):
    """
    A function to find Email from the text using Regular Expression
    created by: Sumit Saurav
    """
    pattern = r"[A-Za-z0-9]+[\._]?[a-z0-9]+[@]\w+[-]?\w+[.]\w{2,3}"
    email = re.findall(pattern, text)
    return email[0] if len(email) > 0 else None


def find_phone(text):
    """
    A function to find phone number from the text using Regular Expression
    created by: Sumit Saurav
    """
    pattern = r"[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}"
    phone = re.findall(pattern, text)
    return phone[0] if len(phone) > 0 else None


def find_name(text):
    """
    This function extracts the name from CV

    Created By: Naveen
    """
    text = text.replace("\n", " ")
    data = nlp(text.lower())
    for entity in data.ents:
        if entity.label_ == "PERSON":
            return entity.text
    
    email = find_email(text)
    if email is not None:
        return email.split("@")[0]
    else:
        return "NA"