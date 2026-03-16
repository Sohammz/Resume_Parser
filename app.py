from flask import Flask, render_template, request
import os

from resume_parser import extract_text
from skill_extractor import extract_skills

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":

        file = request.files["resume"]

        path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(path)

        text = extract_text(path)

        skills = extract_skills(text)

        # ✅ Calculate total skills
        total_skills = sum(len(v) for v in skills.values())

        total_categories = len([c for c in skills if skills[c]])

        return render_template(
            "result.html",
            skills=skills,
            total_skills=total_skills,
            total_categories=total_categories
        )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)