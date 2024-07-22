from flask import Blueprint, request, redirect, url_for, render_template
from .llm import LLM
from datetime import datetime
from .models import Dreams
from .app import db


actions = Blueprint('actions', __name__)

@actions.route('/login', methods=['POST'])
def login():

    user = request.form['username']
    pwd = request.form['password']

    print(f'Usuário: {user}')
    print(f'Senha: {pwd}')

    print('Passou pelo login')

    return 'ok'

@actions.route('/register', methods=['POST','GET'])
def register():
    return render_template('signup.html')


@actions.route('/register_dream', methods=['POST'])
def register_and_analise_dream():
    if request.method == 'POST':
        dream = request.form['dream']
        llm = LLM()

        final_response_text_psicologic = llm.psicologic_analises(dream=dream)
        final_response_resume = llm.resume_analises(dream=dream)
        final_response_imaginary_gestions = llm.imaginary_sugestions(dream=dream)

        date = datetime.now().strftime('%Y%m%d')
        time = datetime.now().strftime('%H:%M')
        new_dream = Dreams(text_dream=dream, date=date, time=time)
        # db.session.add(new_dream)
        # db.session.commit()
        return redirect(url_for('views.view_analysis', dream=dream))
    today_date = datetime.today().strftime('%Y-%m-%d')
    return render_template('index.html', today_date=today_date)