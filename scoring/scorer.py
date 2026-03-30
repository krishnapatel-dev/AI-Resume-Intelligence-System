from sentence_transformers import SentenceTransformer, util
import spacy
import pickle

with open("ml_model/model.pkl", "rb") as f:
    ml_model = pickle.load(f)   # ✅ rename to ml_model
    
nlp = spacy.load("en_core_web_sm")

SKILLS_DB = [
    "python", "java", "sql", "aws",
    "machine learning", "deep learning",
    "react", "node", "mongodb",
    "tensorflow", "flask", "django"
]

# Load model (only once)
model = SentenceTransformer('all-MiniLM-L6-v2')

def calculate_similarity(resume_text, jd_text):
    emb1 = model.encode(resume_text, convert_to_tensor=True)
    emb2 = model.encode(jd_text, convert_to_tensor=True)

    score = util.cos_sim(emb1, emb2)
    return float(score)
def skill_match(resume_skills, required_skills):
    resume_skills = [s.lower() for s in resume_skills]
    required_skills = [s.lower() for s in required_skills]

    matched = list(set(resume_skills) & set(required_skills))
    missing = list(set(required_skills) - set(resume_skills))

    ratio = len(matched) / len(required_skills) if required_skills else 0

    return {
        "matched": matched,
        "missing": missing,
        "skill_score": ratio
    }

import spacy
nlp = spacy.load("en_core_web_sm")

# 🔥 Important known skills
IMPORTANT_SKILLS = {
    "python", "java", "sql", "aws", "react", "node", "mongodb",
    "tensorflow", "flask", "django"
}

def extract_skills(text):
    doc = nlp(text.lower())

    skills = set()

    # NLP-based extraction
    for token in doc:
        if token.pos_ in ["NOUN", "PROPN"]:
            word = token.lemma_

            if (
                len(word) > 2
                and not token.is_stop
                and word not in ["experience", "developer", "project"]
            ):
                skills.add(word)

    # 🔥 Add important skills explicitly
    text_lower = text.lower()
    for skill in IMPORTANT_SKILLS:
        if skill in text_lower:
            skills.add(skill)

    return list(skills)

def final_score(similarity, skill_score, keyword_score, experience_years):
    features = [[
        similarity,
        skill_score,
        keyword_score,
        experience_years
    ]]

    score = ml_model.predict(features)[0]  # ✅ use ml_model

    return round(score, 2)

