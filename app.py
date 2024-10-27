import os
from flask import Flask, render_template, request, redirect, url_for, session
from dotenv import load_dotenv
from questions import questions

load_dotenv() 

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']

def calculate_personality(answers):
    type_counts = {"tipoA": 0, "tipoB": 0, "tipoC": 0, "tipoD": 0, "tipoE": 0}
    for answer in answers:
        type_counts[answer] += 1
    
    return max(type_counts, key=type_counts.get)

@app.route('/')
def home():
    session.clear()
    return render_template('home.html')

@app.route('/instructions')
def instructions():
    return render_template('instructions.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if 'current_question' not in session:
        session['current_question'] = 0
        session['answers'] = []

    current_question = session['current_question']

    if request.method == 'POST':
        selected_type = request.form.get('type')
        session['answers'].append(selected_type)
        session['current_question'] += 1
        current_question = session['current_question']

    if current_question >= len(questions):
        personality = calculate_personality(session['answers'])
        return redirect(url_for('results', personality=personality))
    
    question = questions[current_question]
    return render_template('quiz.html', question=question, question_number=current_question + 1)

@app.route('/results')
def results():
    personality = request.args.get('personality')
    return render_template('results.html', personality=personality)

if __name__ == '__main__':
    app.run(debug=True)
