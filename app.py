<<<<<<< HEAD
from flask import Flask, request, render_template, redirect, jsonify, flash
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "very-secret"

# debug = DebugToolbarExtension(app)

responses = []

@app.route("/")
def show_survey():
  """renders a page to show a survey and a button"""
  return render_template("survey.html", title_in_template=satisfaction_survey.title, instructions_in_template=satisfaction_survey.instructions)
=======
# testing
>>>>>>> refs/remotes/origin/master
