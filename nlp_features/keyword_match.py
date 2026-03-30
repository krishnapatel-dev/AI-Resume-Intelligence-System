import re
from collections import Counter
import spacy
nlp = spacy.load("en_core_web_sm")

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text



def get_keywords(text):
    doc = nlp(text.lower())

    important_pos = {"NOUN", "PROPN", "ADJ"}  # 🔥 KEY CHANGE
    generic_words = {"experience", "developer", "job", "role"}

    keywords = [
        token.lemma_
        for token in doc
        if not token.is_stop
        and token.is_alpha
        and token.pos_ in important_pos
        and token.lemma_ not in generic_words
        and len(token.lemma_) > 2
    ]

    return Counter(keywords)


def keyword_match_score(resume_text, jd_text):
    resume_keywords = get_keywords(resume_text)
    jd_keywords = get_keywords(jd_text)

    matched_keywords = set(jd_keywords.keys()) & set(resume_keywords.keys())

    matched = len(matched_keywords)
    total = len(jd_keywords)
    
    # 🔥 Balanced scoring
    if total == 0:
        score = 0
    else:
        score = matched / total
    
    # Boost score if at least one strong match exists
    if matched > 0:
        score = min(score + 0.2, 1.0)

    return {
        "keyword_score": round(score * 100, 2),
        "matched_keywords": list(set(jd_keywords.keys()) & set(resume_keywords.keys()))
    }