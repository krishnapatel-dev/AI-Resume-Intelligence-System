import re

def generate_feedback(text):
    feedback = []
    text_lower = text.lower()

    # 1. Measurable achievements
    if not re.search(r'\d+', text):
        feedback.append("Add measurable achievements (e.g., increased performance by 20%)")
    else:
        feedback.append("Good: You have included measurable achievements 👍")

    # 2. Resume length
    word_count = len(text.split())
    if word_count < 150:
        feedback.append("Resume is too short, add more details")
    elif word_count > 1000:
        feedback.append("Resume is too long, try to keep it concise")
    else:
        feedback.append("Good: Resume length is well balanced 👍")

    # 3. Weak phrases
    weak_phrases = ["responsible for", "worked on", "helped with"]
    found_weak = False

    for phrase in weak_phrases:
        if phrase in text_lower:
            feedback.append(f"Avoid weak phrase: '{phrase}', use strong action verbs")
            found_weak = True

    if not found_weak:
        feedback.append("Good: Strong action-oriented language used 👍")

    # 4. Skills section
    if "skills" not in text_lower:
        feedback.append("Add a dedicated skills section")
    else:
        feedback.append("Good: Skills section is present 👍")

    # 5. Action verbs
    strong_verbs = ["developed", "built", "designed", "implemented", "led"]
    if not any(verb in text_lower for verb in strong_verbs):
        feedback.append("Use strong action verbs like Developed, Built, Led")
    else:
        feedback.append("Good: Strong action verbs detected 👍")

    return feedback