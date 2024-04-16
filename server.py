from flask import Flask, render_template, request

app = Flask(__name__)

# Home page with a Start button
@app.route('/')
def home():
    return render_template('home.html')  # Assuming you have a home.html file with a Start button

# Learning page that takes a lesson number variable
@app.route('/learn/<int:lesson_number>')
def learn(lesson_number):
    return render_template('lesson.html', lesson_number=lesson_number)  # Pass the lesson number to the template

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

if __name__ == '__main__':
    app.run(debug=True)
