from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "just-my-secret"

responses = []

@app.route('/')
def survey_start():


    return render_template('survey.html', title=satisfaction_survey.title, instructions=satisfaction_survey.instructions)