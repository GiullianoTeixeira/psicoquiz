# TODO: RETHINK THIS APPROACH
# from flask import Blueprint, render_template, request, redirect, url_for, session
# from collections import Counter
# from questions import questions
# from logic import *

# quiz_bp = Blueprint('quiz', __name__)

# @quiz_bp.route('/')
# def home():
#     return render_template('home.html')

# @quiz_bp.route('/quiz/<int:question_index>', methods=['GET', 'POST'])
# def quiz(question_index):
#     if 'answers' not in session:
#         session['answers'] = []

#     if request.method == 'POST':
#         selected_option = int(request.form['option'])
#         session['answers'].append(questions[question_index]['options'][selected_option]['traits'])

#         if question_index + 1 < len(questions):
#             return redirect(url_for('quiz.quiz', question_index=question_index + 1))
#         else:
#             return redirect(url_for('quiz.results'))

#     return render_template('quiz.html', question=questions[question_index], question_index=question_index)

# @quiz_bp.route('/results')
# def results():
#     trait_counts = Counter()
#     for answer in session['answers']:
#         trait_counts.update(answer)

#     threshold = 7
#     dominant_trait = None
#     for trait, count in trait_counts.items():
#         if count >= threshold:
#             dominant_trait = trait
#             break

#     if dominant_trait:
#         return render_template('results.html', result=f"You are predominantly {dominant_trait}")
#     else:
#         return render_template('results.html', result="No dominant trait detected")
