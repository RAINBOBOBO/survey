from flask import Flask, request, render_template, redirect, jsonify, flash, session
from flask_debugtoolbar import DebugToolbarExtension
# from surveys import satisfaction_survey #TODO: uncomment later

app = Flask(__name__)
app.config['SECRET_KEY'] = "SHHHHHHHHHHH SEEKRIT"

# debug = DebugToolbarExtension(app)

# responses = []

# for reference only TODO: delete later
class Question:
    def __init__(self, question, choices=None, allow_text=False):
        if not choices:
            choices = ["Yes", "No"]

        self.question = question
        self.choices = choices
        self.allow_text = allow_text


class Survey:
    def __init__(self, title, instructions, questions):
        self.title = title
        self.instructions = instructions
        self.questions = questions

satisfaction_survey = Survey(
    "Customer Satisfaction Survey",
    "Please fill out a survey about your experience with us.",
    [
        Question("Have you shopped here before?"),
        Question("Did someone else shop with you today?"),
        Question("On average, how much do you spend a month on frisbees?",
                 ["Less than $10,000", "$10,000 or more"]),
        Question("Are you likely to shop here again?"),
    ])

@app.route("/")
def show_survey():
  """renders a page to show a survey and a button"""
  return render_template("survey.html", title_in_template=satisfaction_survey.title, instructions_in_template=satisfaction_survey.instructions)


@app.route("/start-session", methods=["POST"])
def start_session():
  """setup a new session then redirect to survey"""
  session['responses'] = []
  return redirect('/questions/0')



@app.route("/questions/<str_question>")
def show_questions(str_question):
    """shows questions"""
    num_question = int(str_question)

    if num_question != len(session['responses']):
        flash("Follow the rules pls")
        return redirect(f"/questions/{len(session['responses'])}")

    return render_template("questions.html",
        question_in_template = satisfaction_survey.questions[num_question],
        num_question_in_template = num_question,
        choices_in_template = satisfaction_survey.questions[num_question].choices)



@app.route("/answer", methods=["POST"])
def answer():
    session['responses'] = session['responses'] + [request.form["question-radio"]]
    next_question = request.form["question-radio"][-1]

    if int(next_question)+1 >= len(satisfaction_survey.questions):
        return redirect("/thanks")
    else:
        return redirect(f"/questions/{str(int(next_question)+1)}")


@app.route("/thanks")
def thanks():
    return render_template("thanks.html")