import re
import requests
from collections import Counter


def extract_github_username(text):
    match = re.search(r'github\.com/([A-Za-z0-9_-]+)', text)

    if match:
        return match.group(1)

    return None



def get_github_data(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)

    if response.status_code != 200:
        return {"error": "GitHub user not found"}

    data = response.json()

    # 🔥 NEW PART: Fetch repositories
    repos_url = f"https://api.github.com/users/{username}/repos"
    repos_response = requests.get(repos_url)

    top_languages = []

    if repos_response.status_code == 200:
        repos = repos_response.json()
    
        lang_list = [
            repo.get("language")
            for repo in repos
            if repo.get("language")
        ]
    
        top_languages = [
            lang for lang, _ in Counter(lang_list).most_common(5)
        ]

    return {
        "username": username,
        "public_repos": data.get("public_repos"),
        "followers": data.get("followers"),
        "following": data.get("following"),
        "profile_url": data.get("html_url"),
        "top_languages": top_languages
    }
def github_enrichment(text):
    username = extract_github_username(text)

    if not username:
        return {"message": "No GitHub profile found"}

    return get_github_data(username)
