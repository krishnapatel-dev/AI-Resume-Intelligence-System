import re
import spacy

nlp = spacy.load("en_core_web_sm")

def preprocess_text(text):
    # 1. Basic cleaning (safe)
    text = text.lower()
    text = re.sub(r'http\S+', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()

    # 2. NLP processing
    doc = nlp(text)

    tokens = [
        token.lemma_
        for token in doc
        if not token.is_stop
        and not token.is_punct
        and token.is_alpha
    ]

    return " ".join(tokens)