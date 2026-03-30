from flask import Flask, request, jsonify
from parser.main_parser import parse_resume
from section_detector.detector import detect_sections
from scoring.scorer import calculate_similarity, extract_skills, skill_match, final_score
from feedback.feedback import generate_feedback
from enrichment.github import github_enrichment
from nlp_features.experience import calculate_experience
from nlp_features.keyword_match import keyword_match_score
from nlp_features.summarizer import simple_summary
from utils.preprocessing import preprocess_text

HEADINGS = {
    "education": ["education", "academic"],
    "experience": ["experience", "work", "internship"],
    "skills": ["skills", "technical skills"],
    "projects": ["projects"]
}

app = Flask(__name__)

@app.route("/")
def home():
    return "Resume Parser Running"

@app.route("/parse", methods=["POST"])
def parse():
    if "resume" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["resume"]

    try:
        text = parse_resume(file)
        sections = detect_sections(text)

        return jsonify({
            "extracted_text": text[:1000],
            "sections": sections
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500
    
@app.route("/analyze", methods=["POST"])
def analyze():
    
    file = request.files["resume"]
    jd = request.form["job_description"]

    
    text = parse_resume(file)

    # Step 1: Section detection (RAW TEXT)
    sections = detect_sections(text)
    
    # Step 2: Create relevant text
    relevant_text = " ".join(
        sections.get("skills", []) +
        sections.get("experience", []) +
        sections.get("projects", [])
    )
    
    # Step 3: Apply preprocessing ONLY HERE
    clean_resume = preprocess_text(relevant_text)
    clean_jd = preprocess_text(jd)
    
    # Step 4: Use in similarity
    similarity = calculate_similarity(clean_resume, clean_jd)
    sections = detect_sections(text)

    resume_skills = extract_skills(text)
    required_skills = extract_skills(jd)
    
    experience_text = " ".join(sections.get("experience", []))
    experience_years = calculate_experience(experience_text)

    # Extract only important lines (short + relevant)
    skills_text = " ".join(sections.get("skills", []))
    projects_text = " ".join(sections.get("projects", [])[:2])  # only top 2
    experience_text = " ".join(sections.get("experience", [])[:5])  # first few lines
    
    relevant_text = f"{skills_text} {projects_text} {experience_text}"
    
    similarity = calculate_similarity(relevant_text, jd)
    skill_data = skill_match(resume_skills, required_skills)
    
    
    keyword_data = keyword_match_score(text, jd)

    feedback = generate_feedback(text)
    
    summary = simple_summary(sections)
    
    score = final_score(
        similarity,
        skill_data["skill_score"],
        keyword_data["keyword_score"],
        experience_years
    )

    # NEW FEATURE 👇
    github_data = github_enrichment(text)

    return jsonify({
        "score": score,
        "skills": skill_data,
        "sections": sections,
        "feedback": feedback,
        "github": github_data,
        "experience_years": experience_years,
        "keyword_analysis": keyword_data,
        "summary": summary,
        "score_breakdown": {
            "similarity": similarity,
            "skill_score": skill_data["skill_score"],
            "keyword_score": keyword_data["keyword_score"],
            "experience": experience_years
        }
    })


if __name__ == "__main__":
    #app.run(debug=True)
    app.run(debug=True, use_reloader=False)