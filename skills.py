skills_list = [
    "python",
    "sql",
    "machine learning",
    "deep learning",
    "power bi",
    "tableau",
    "excel",
    "pandas",
    "numpy",
    "tensorflow",
    "scikit-learn"
]

def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in skills_list:

        if skill in text:

            found_skills.append(skill)

    return found_skills