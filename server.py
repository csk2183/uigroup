from flask import Flask, render_template, request, redirect, url_for, session
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'rule11key'

quiz_questions = [
    {
        "question_id": 1,
        "question_text": "What is considered offside position in soccer?",
        "options": [
            "Being in the opponent’s half of the field.",
            "Being behind the ball when it is played.",
            "Being nearer to the opponent's goal than both the ball and the second last opponent when the ball is played to them.",
            "Standing in the goalkeeper’s area."
        ],
        "answer": "3",
        "userAnswer": None
    },
    {
        "question_id": 2,
        "question_text": "When does being in an offside position lead to an offside rules offense?",
        "options": [
            "At any time during the game when the player is in the offside position.",
            "When the player is in the offside position and actively interferes with play.", 
            "When the player is passively standing on the field.", 
            "Only during a corner kick."
        ],
        "answer": "2",
        "userAnswer": None
    },
    {
        "question_id": 3,
        "question_text": "When is a player not considered offside?",
        "options": [
            "When receiving the ball directly from a goal kick.", 
            "When they are in their own half of the pitch.", 
            "Receiving a throw in from while standing behind second-last defender.", 
            "All of the above."
        ],
        "answer": "4",
        "userAnswer": None
    },
    {
        "question_id": 4,
        "question_text": "What determines whether a player is offside when the ball is played to them?",
        "options": [
            "The position of the ball only.",
            "The position of the player and the second last opponent at the moment the ball is played.",
            "The position of the player when the play starts.",
            "The referee’s discretion without any specific criteria."
        ],
        "answer": "2",
        "userAnswer": None
    },
    {
        "question_id": 5,
        "question_text": "In which area of the field can a player never be offside?",
        "options": [
            "In the opponent's penalty area.",
            "In the center circle.",
            "In their own half of the field.",
            "In the goal area."
        ],
        "answer": "3",
        "userAnswer": None
    },
    {
        "question_id": 6,
        "question_text": "The attacking goalie does a goal kick towards a player behind the second defender. The attacking player then scores!",
        "options": [
            "Offside Call",
            "No Offside Call"
        ],
        "answer": "2",
        "userAnswer": None,
        "image_path": "/static/data/learning/Question6.png"
    }
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

@app.route('/quiz/intro')
def quiz_intro():
    global quiz_questions
    for question in quiz_questions:
        question["userAnswer"] = None
    return render_template('quiz_intro.html')

@app.route('/quiz/<int:question_id>')
def quiz(question_id):
    if question_id > len(quiz_questions):
        return redirect(url_for('quiz_results'))

    question = quiz_questions[question_id - 1]
    last_question = question_id==len(quiz_questions)
    return render_template('quiz.html', question=question, question_id=question_id, last_question=last_question)

@app.route('/quiz/modify_user_answer', methods=['POST'])
def quiz_modify_user_answers():
    global quiz_questions
    data = request.get_json()
    answer = data.get('userAnswer')
    question_number = int(data.get('question_number'))
    index = question_number - 1
    if 0 <= index < len(quiz_questions):
        quiz_questions[index]["userAnswer"] = answer
        return 'User answer modified successfully.', 200
    else:
        return 'Error: Question number out of range.', 400
    
@app.route('/quiz/results')
def quiz_results():
    results = []
    for question in quiz_questions:
        if question['userAnswer'] != None:
            results.append({
                'question_text': question['question_text'],
                'user_answer': question['options'][int(question['userAnswer']) - 1],
                'correct_answer': question['options'][int(question['answer']) - 1],
                'correct': question['answer'] == question['userAnswer']
            })

    score = 0
    for question in quiz_questions:
        if question["answer"] == question["userAnswer"]:
            score += 1

    if len(results) == 0:
        return redirect(url_for('quiz_intro'))

    return render_template('results.html', score=score, total=len(quiz_questions), results=results)

if __name__ == '__main__':
    app.run(debug=True)
