import re
from flask import Flask, redirect, render_template, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "just-my-secret"



title=satisfaction_survey.title
instructions=satisfaction_survey.instructions
current_q = 0

@app.route('/')
def survey_start():

    return render_template('survey.html', title=title, instructions=instructions)

@app.route('/new_session', methods=["POST"])
def new_session():
    session["responses"] = []

    return redirect("/questions/0")

@app.route('/answers', methods=["POST"])
def answers():
    global current_q
    answer = request.form[f"q{current_q}"]
    responses = session["responses"]
    responses.append(answer)
    session["responses"] = responses
    
    current_q += 1

    return redirect(f"/questions/{current_q}")

@app.route('/questions/<int:q_num>')
def question(q_num):
    if q_num == current_q:
        if q_num >= len(satisfaction_survey.questions):
            return redirect('/thanks')
        else:
            question = satisfaction_survey.questions[q_num].question
            choices = satisfaction_survey.questions[q_num].choices

            return render_template('question.html', question = question, choices = choices, title=title, q_num=q_num )
    else:
        flash("you were trying to visit the wrong page, now you're back where you should be", "warning")
        return redirect(f"/questions/{current_q}")

@app.route('/thanks')
def thanks():
    responses = session["responses"]
    return render_template('thanks.html', title=title)