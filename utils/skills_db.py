SKILLS_DB = [
    "python", "java", "sql", "aws",
    "machine learning", "deep learning",
    "react", "node.js", "mongodb"
]

import spacy
nlp = spacy.load("en_core_web_sm")

def extract_skills(text):
    doc = nlp(text.lower())
    found_skills = set()

    for token in doc:
        for skill in SKILLS_DB:
            if skill in token.text:
                found_skills.add(skill)

    return list(found_skills)