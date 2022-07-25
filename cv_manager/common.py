import re
import os
import spacy
import sqlite3
from db_manager.query import dictfetchall
from db_manager import DB

nlp = spacy.load("en_core_web_lg")
skills_model = os.path.join(os.getcwd(), "skills_model")

def get_skills(text):
    doc = nlp(text)
    myset = []
    subset = []
    for ent in doc.ents:
        if ent.label_ == "SKILL":
            subset.append(ent.text)
    myset.append(subset)
    return subset

def find_skills(text):
    """
    A function to find Skills from the text using Regular Expression
    created by: Sumit Saurav
    """
    try:
        nlp = spacy.load(skills_model)
        doc = nlp(text)
        skills = get_skills(doc)
        return ", ".join(list(set(skills)))
    except Exception as e:
        print("Error while finding skills: ", e)


def find_email(text):
    """
    A function to find Email from the text using Regular Expression
    created by: Sumit Saurav
    """
    try:
        pattern = r"[A-Za-z0-9]+[\._]?[a-z0-9]+[@]\w+[-]?\w+[.]\w{2,3}"
        email = re.findall(pattern, text)
        return email[0].lower() if len(email) > 0 else None
    except Exception as e:
        print(e)


def find_phone(text):
    """
    A function to find phone number from the text using Regular Expression
    created by: Sumit Saurav
    """
    try:
        pattern = r"[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}"
        phone = re.findall(pattern, text)
        return phone[0] if len(phone) > 0 else None
    except Exception as e:
        print(e)


def find_name(text):
    """
    This function extracts the name from CV

    Created By: Naveen
    """
    try:
        text = text.replace("\n", " ")
        data = nlp(text.lower())
        for entity in data.ents:
            if entity.label_ == "PERSON" and bool(re.search(r"\d", entity.text)) == False:
                name = entity.text

        email = find_email(text)
        if email is not None:
            name = email.split("@")[0]
        else:
            name = "NA"
        
        if "@" in name:
            return name.split("@")[0]
        else:
            return name
    except Exception as e:
        print(e)

def find_category(id):

    BACKEND = ["python", "java", "node", "express", "django", "spring boot", "php"]
    FRONTEND = ["css", "html", "js", "javascript"]
    FULLSTACK = BACKEND + FRONTEND
    MARKETING = ["marketing", "sales", "branding"]
    DESIGNER = ["photoshop", "adobe", "designing", "graphic", "figma", "illustrator"]
    DATA_SCIENCE = ["data science", "machine learning", "ai", "regression", "classification"]
    ACCOUNTANT = ["accounting", "account", "payroll"]

    skill_mapping = {
        "BACKEND": 0,
        "FRONTEND": 0,
        "MARKETING": 0,
        "DESIGNER": 0,
        "DATA_SCIENCE": 0,
        "FULLSTACK": 0,
        "ACCOUNTANT": 0
    }

    conn = sqlite3.connect(DB)
    curr = conn.cursor()
    curr.execute("SELECT * FROM user where id = {};".format(id))
    data = dictfetchall(curr)
    
    for i in data:
        for sk in i['skills'].split(","):
            if sk.lower().strip() in BACKEND:
                skill_mapping["BACKEND"] += 1
            if sk.lower().strip() in FRONTEND:
                skill_mapping["FRONTEND"] += 1
            if sk.lower().strip() in MARKETING:
                skill_mapping["MARKETING"] += 1
            if sk.lower().strip() in DESIGNER:
                skill_mapping["DESIGNER"] += 1
            if sk.lower().strip() in DATA_SCIENCE:
                skill_mapping["DATA_SCIENCE"] += 1
            if sk.lower().strip() in FULLSTACK:
                skill_mapping["FULLSTACK"] += 1
            if sk.lower().strip() in ACCOUNTANT:
                skill_mapping['ACCOUNTANT'] += 1
    
    fin_max = max(skill_mapping, key=skill_mapping.get)
    print(fin_max)
    curr.execute("SELECT id from category where name = '{}' limit 1".format(fin_max))
    data = curr.fetchone()
    if len(data) > 0:
        category_id = data[0]
        print(category_id)
        curr.execute("UPDATE user set category_id = {} where id = {}".format(category_id, id))
        conn.commit()
    conn.close()
    return skill_mapping