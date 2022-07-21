import re
# Create function to extract skills from CV
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
    skills = []
    for i in skills:
        pattern = re.compile(i)
        if bool(re.search(pattern, text.lower())):
            skills.append(i)
    return skills

# Create a function to extract email id from CV

# Create a function to extract Phone number from CV

# Create a function to extract Name from CV