from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime


app = Flask(__name__)

# Temporary quiz questions data structure
quiz_questions = [
    {
        "question_id": 1,
        "question_text": "When is a player not considered offside?",
        "options": ["When receiving the ball directly from a goal kick.", "When they are in their own half of the pitch.", "Receiving a throw in from while standing behind second-last defender.", "All of the above."],
        "answer": "All of the above."
    },
    {
        "question_id": 2,
        "question_text": "A defender's attempted clearance mis-hits to a forward who was in an offside position at the time the ball was played. The forward then scores. Is the goal allowed?",
        "options": ["Yes, because the ball came from an opponent.", "No, because the forward was in an offside position.", "Yes, but only if the referee determines the defender played the ball deliberately.", "No, unless the ball was played to the forward by a teammate."],
        "answer": "Yes, but only if the referee determines the defender played the ball deliberately."
    },
    {
        "question_id": 3,
        "question_text": "The attacking goalie does a goal kick towards a player behind the second defender. The attacking player then scores",
        "options": ["Offside Call", "No Offside Call"],
        "answer": "No Offside Call"
    },
]

# Home page with a Start button
@app.route('/')
def home():
    return render_template('home.html')
    access_time = datetime.now()  # Capture the current time
    print(f"Basics home page accessed at {access_time}")
    return render_template('home.html')  # Assuming you have a home.html file with a Start button

# Learning page that takes a lesson number variable
@app.route('/basics')
def basics():
    access_time = datetime.now()  # Capture the current time
    print(f"Basics page accessed at {access_time}")
    return render_template('basics.html')

@app.route('/offside-explained')
def offside_explained():
    access_time = datetime.now()  # Capture the current time
    print(f"Offsides explained page accessed at {access_time}")
    return render_template('offside-explained.html')

@app.route('/exceptions')
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
        # Redirect to results if it's the last question
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
