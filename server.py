<<<<<<< HEAD
from flask import Flask, render_template, request, redirect, url_for
=======
from flask import Flask, render_template, request
from datetime import datetime
>>>>>>> 1e825e5dc208990ffaae86945ff1cb1ab47b26e7

app = Flask(__name__)

# Temporary quiz questions data structure
quiz_questions = [
    {
        "question_id": 1,
        "question_text": "Question 1 text",
        "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
        "answer": "Option 1"
    },
    {
        "question_id": 2,
        "question_text": "Question 2 text",
        "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
        "answer": "Option 2"
    },
    {
        "question_id": 3,
        "question_text": "Question 3 text",
        "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
        "answer": "Option 3"
    },
]

# Home page with a Start button
@app.route('/')
def home():
<<<<<<< HEAD
    return render_template('home.html')
=======
    access_time = datetime.now()  # Capture the current time
    print(f"Basics home page accessed at {access_time}")
    return render_template('home.html')  # Assuming you have a home.html file with a Start button
>>>>>>> 1e825e5dc208990ffaae86945ff1cb1ab47b26e7

# Learning page that takes a lesson number variable
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
