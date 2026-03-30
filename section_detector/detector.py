HEADINGS = {
    "education": ["education", "academic", "qualification"],
    "experience": ["experience", "work", "employment", "internship"],
    "skills": ["skills", "technical", "technologies"],
    "projects": ["projects", "project work"],
    "certifications": ["certifications", "certificates"]
}

def detect_sections(text):
    sections = {k: [] for k in HEADINGS}
    sections["other"] = []

    current_section = "other"

    for line in text.split("\n"):
        original_line = line.strip()
        clean = original_line.lower().strip()

        # Normalize
        clean = clean.replace(":", "").strip()

        # 🔥 Detect headings safely
        if len(clean.split()) <= 4:   # allow "work experience"
            for section, keywords in HEADINGS.items():
                for keyword in keywords:
                    # ✅ match full phrase OR strong partial match
                    if clean == keyword or keyword in clean:
                        current_section = section
                        break
                else:
                    continue
                break

        # Add content
        if original_line:
            sections[current_section].append(original_line)

    return sections