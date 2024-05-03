from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime


app = Flask(__name__)

# Temporary quiz questions data structure
quiz_questions = [
    {
        "question_id": 1,
        "question_type": "multiple_choice",
        "question_text": "What is considered offside position in soccer?",
        "options": [
            "Being in the opponent’s half of the field.",
            "Being behind the ball when it is played.",
            "Being nearer to the opponent's goal than both the ball and the second last opponent when the ball is played to them.",
            "Standing in the goalkeeper’s area."
        ],
        "answer": "3"
    },
    {
        "question_id": 2,
        "question_type": "multiple_choice",
        "question_text": "When does being in an offside position lead to an offside rules offense?",
        "options": [
            "At any time during the game when the player is in the offside position.",
            "When the player is in the offside position and actively interferes with play.", 
            "When the player is passively standing on the field.", 
            "Only during a corner kick."
        ],
        "answer": "2"
    },
    {
        "question_id": 3,
        "question_type": "multiple_choice",
        "question_text": "When is a player not considered offside?",
        "options": [
            "When receiving the ball directly from a goal kick.", 
            "When they are in their own half of the pitch.", 
            "Receiving a throw in from while standing behind second-last defender.", 
            "All of the above."
        ],
        "answer": "4"
    },
    {
        "question_id": 4,
        "question_type": "multiple_choice",
        "question_text": "What determines whether a player is offside when the ball is played to them?",
        "options": [
            "The position of the ball only.",
            "The position of the player and the second last opponent at the moment the ball is played.",
            "The position of the player when the play starts.",
            "The referee’s discretion without any specific criteria."
        ],
        "answer": "2"
    },
    {
        "question_id": 5,
        "question_type": "multiple_choice",
        "question_text": "In which area of the field can a player never be offside?",
        "options": [
            "In the opponent's penalty area.",
            "In the center circle.",
            "In their own half of the field.",
            "In the goal area."
        ],
        "answer": "3"
    },
]

# Home page with a Start button
@app.route('/')
def home():
    return render_template('home.html')

# Learning page that takes a lesson number variable
@app.route('/learning/basics')
def basics():
    access_time = datetime.now()  # Capture the current time
    print(f"Basics page accessed at {access_time}")
    return render_template('basics.html')

@app.route('/learning/offside-explained')
def offside_explained():
    access_time = datetime.now()  # Capture the current time
    print(f"Offsides explained page accessed at {access_time}")
    return render_template('offside-explained.html')

@app.route('/learning/exceptions')
def exceptions():
    access_time = datetime.now()  # Capture the current time
    print(f"Exceptions page accessed at {access_time}")
    return render_template('exceptions.html')


"""
# Quiz page that takes a quiz number variable
@app.route('/quiz/<int:quiz_number>')
def quiz(quiz_number):
    return render_template('quiz.html', quiz_number=quiz_number)  # Pass the quiz number to the template


# Quiz results page
@app.route('/results', methods=['POST'])
def results():
    # For simplicity, assuming results are sent via POST request
    data = request.form
    # Process results here (e.g., calculate score)
    return render_template('results.html', results=data)  # Pass results to the template
"""

@app.route('/quiz/intro')
def quiz_intro():
    return render_template('quiz_intro.html')


@app.route('/quiz/<int:question_id>', methods=['GET', 'POST'])
def quiz(question_id):
    answers = ''
    if request.method == 'POST':
        # Retrieve the current and previous answers
        answers = request.form.get('answers', '')
        user_answer = request.form.get('user_answer', '')
        if user_answer:
            answers += user_answer

    if question_id > len(quiz_questions):
        return redirect(url_for('quiz_results', answers=answers))

    question = quiz_questions[question_id - 1]
    return render_template('quiz.html', question=question, question_id=question_id, answers=answers)

@app.route('/quiz/results')
def quiz_results():
    answers = request.args.get('answers', '')
    score = sum(1 for i, answer in enumerate(answers, start=1) if quiz_questions[i-1]['answer'] == quiz_questions[i-1]['options'][int(answer)-1])
    return render_template('results.html', score=score, total=len(quiz_questions))

if __name__ == '__main__':
    app.run(debug=True)
