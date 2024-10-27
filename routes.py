from flask import render_template, request, redirect, url_for, session
from questions import questions
from logic import *

def setup_routes(app):
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
            session['answers'] = {"tipoA": 0, "tipoB": 0, "tipoC": 0, "tipoD": 0, "tipoE": 0}

        current_question = session['current_question']

        if request.method == 'POST':
            selected_option = request.form.get('option') 
            if selected_option is not None:
                selected_option = int(selected_option)
                selected_types = questions[current_question]['options'][selected_option]['types']
                for trait, value in selected_types.items():
                    session['answers'][trait] += value
            
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
