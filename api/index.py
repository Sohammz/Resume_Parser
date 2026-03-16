from flask import Flask, render_template, request
import os

from resume_parser import extract_text
from skill_extractor import extract_skills

app = Flask(__name__, template_folder="../templates", static_folder="../static")

UPLOAD_FOLDER = "/tmp"

@app.route("/", methods=["GET", "POST"])
def index():

    skills = {}

    if request.method == "POST":

        file = request.files["resume"]

        path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(path)

        text = extract_text(path)

        skills = extract_skills(text)

    return render_template("index.html", skills=skills)


# Required for Vercel
def handler(request):
    return app