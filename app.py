from surveys import satisfaction_survey
from flask import Flask, render_template, request, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
debug = DebugToolbarExtension(app)

quiz = satisfaction_survey
responses = []
quest_replied = []
num_questions = len(quiz.questions)
count = f"/questions/{len(quest_replied)}"

@app.route('/')
def main():
    """Welcome page"""
    return render_template("base.html", quiz=quiz, quest_replied=quest_replied)

@app.route('/questions/0')
def question():
    if len(quest_replied) == 0:
        return render_template("questions/0.html", quiz=quiz)
    else:
        flash("You have been re-directed!")
        return redirect(f"/questions/{len(quest_replied)}")

@app.route('/questions/1')
def question1():
    if len(quest_replied) == 1:
        return render_template("questions/1.html", quiz=quiz)
    else:
        flash("You have been re-directed!")
        return redirect(f"/questions/{len(quest_replied)}")

@app.route('/questions/2')
def question2():
    if len(quest_replied) == 2:
        return render_template("questions/2.html", quiz=quiz)
    else:
        flash("You have been re-directed!")
        return redirect(f"/questions/{len(quest_replied)}")

@app.route('/questions/3')
def question3():
    if len(quest_replied) == 3:
        return render_template("questions/3.html", quiz=quiz)
    else:
        flash("You have been re-directed!")
        return redirect(f"/questions/{len(quest_replied)}")

@app.route("/answer", methods=["POST"])
def answers():
    if (num_questions -1) > len(quest_replied):
        ans = request.form["choices"]
        responses.append(ans)
        quest_replied.append("replied")
        count = f"/questions/{len(quest_replied)}"
        return redirect(count)
    else:
        ans = request.form["choices"]
        responses.append(ans)
        quest_replied.append("replied")
        return render_template("/thanks.html", res = responses)
    