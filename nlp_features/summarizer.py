def simple_summary(sections):
    summary_parts = []

    # Experience
    if "experience" in sections and sections["experience"]:
        summary_parts.append("Experienced in full-stack and machine learning development.")

    # Skills
    if "skills" in sections and sections["skills"]:
        skills_line = sections["skills"][0]
        summary_parts.append(f"Skilled in {skills_line[:100]}.")

    # Projects
    if "projects" in sections and sections["projects"]:
        summary_parts.append("Worked on multiple projects involving AI, web development, and IoT.")

    return " ".join(summary_parts)