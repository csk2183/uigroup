from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

# Home page with a Start button
@app.route('/')
def home():
    access_time = datetime.now()  # Capture the current time
    print(f"Basics home page accessed at {access_time}")
    return render_template('home.html')  # Assuming you have a home.html file with a Start button

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
