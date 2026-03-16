import spacy
from skills_db import skills

nlp = spacy.load("en_core_web_sm")

def extract_skills(text):

    doc = nlp(text)

    extracted = {}

    for category in skills:

        extracted[category] = []

        for skill in skills[category]:

            if skill.lower() in text:
                extracted[category].append(skill)

    return extracted