from flask import Flask, render_template, request, redirect, url_for
from questions import quiz_data
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    #quizis kategoriebi
    categories = quiz_data.keys()
    current_year = datetime.now().year
    return render_template("index.html", categories=categories, year=current_year)

@app.route("/quiz/<category>", methods=["GET", "POST"])
def quiz(category):
    #question to display the selected questions"
    if category not in quiz_data:
        return redirect(url_for("index"))

    questions=quiz_data[category]

    if request.method=="POST":
        user_answers=request.form
        score=0
        correct_answers=[]

        # Evaluate user's answers
        for i, question in enumerate(questions):
            user_answer=user_answers.get(f"q{i}")
            correct_answer=question["answer"]
            if user_answer==correct_answer:
                score+=1
            correct_answers.append({
                "question": question["question"],
                "correct": correct_answer,
                "user": user_answer or "No Answer"
            })

        current_year=datetime.now().year
        return render_template(
            "result.html",
            category=category,
            score=score,
            total=len(questions),
            correct_answers=correct_answers,
            year=current_year
        )

    current_year=datetime.now().year
    return render_template(
        "quiz.html",
        category=category,
        questions=questions,
        enumerate=enumerate,
        year=current_year
    )
#mtavari kodis gamshvebi
if __name__ == "__main__":
    app.run(debug=True)
