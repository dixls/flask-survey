from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "just-my-secret"

responses = []
title=satisfaction_survey.title
instructions=satisfaction_survey.instructions
current_q = 0

@app.route('/')
def survey_start():

    return render_template('survey.html', title=title, instructions=instructions)

@app.route('/questions/0')
def question_0():
    question = satisfaction_survey.questions[0].question
    choices = satisfaction_survey.questions[0].choices

    return render_template('question_0.html', question = question, choices = choices, title=title )

@app.route('/answers', methods=["POST"])
def answers():
    