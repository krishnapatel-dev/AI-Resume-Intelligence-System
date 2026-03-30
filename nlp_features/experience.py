from datetime import datetime
import re

def calculate_experience(text):
    # Match patterns like "Jan 2025 – Apr 2025"
    matches = re.findall(r'(\w+\s\d{4})\s[–-]\s(\w+\s\d{4})', text)

    total_months = 0

    for start, end in matches:
        try:
            start_date = datetime.strptime(start, "%b %Y")
            end_date = datetime.strptime(end, "%b %Y")

            diff = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
            total_months += diff

        except:
            continue

    return round(total_months / 12, 2)