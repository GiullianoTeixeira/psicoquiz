from flask import render_template, request, redirect, url_for, session
from content.questions import questions
from text import traits
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
            session['answers'] = {tipo: 0 for tipo in traits}

        current_question = session['current_question']

        if request.method == 'POST':
            selected_option = request.form.get('option') 
            if selected_option is not None:
                selected_option = int(selected_option)
                selected_traits = questions[current_question]['options'][selected_option]['traits']
                for trait, value in selected_traits.items():
                    session['answers'][trait] += value
            
            session['current_question'] += 1
            current_question = session['current_question']

        if current_question >= len(questions):
            result, title = final_result(session['answers'])
            session['result'] = result
            session['title'] = title
            return redirect(url_for('results'))

        question = questions[current_question]
        return render_template('quiz.html', question=question, question_number=current_question + 1)

    @app.route('/results')
    def results():
        result = session.get('result', [])
        title = session.get('title', '')
        return render_template('results.html', result=result, title=title, body_background_color='rgb(177, 156, 217)')