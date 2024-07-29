from flask import Blueprint, request, redirect, url_for, render_template, flash, session
from .llm import LLM
from datetime import datetime
from .models import Dreams, Users
from .app import db
import markdown
from werkzeug.security import generate_password_hash, check_password_hash

actions = Blueprint('actions', __name__)

@actions.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        pwd = request.form['password']
        
        print(f'Received login request for user: {user}')
        
        # Autenticar o usuário
        user_record = Users.query.filter_by(user_name=user).first()
        if user_record:
            print(f'User found in database: {user_record.user_name}')
        else:
            print('User not found in database')

        if user_record and check_password_hash(user_record.user_pwd_hash, pwd):
            session['user_id'] = user_record.id
            session['user_name'] = user_record.user_name
            flash('Login bem-sucedido!')
            return redirect(url_for('views.index'))
        else:
            flash('Nome de usuário ou senha incorretos. Tente novamente.')
            return redirect(url_for('actions.login'))
    return render_template('index.html')


@actions.route('/register', methods=['POST', 'GET'])
def register():
    print('Aqui')
    print(f'Analisado -> {request}')
    try:
        user_name = request.form['username']
        user_email = request.form['email']
        user_pwd = request.form['password']
        user_profession = request.form['profession']
        
        # Hashing the password
        user_pwd_hash = generate_password_hash(user_pwd)
        
        # Checking if user already exists
        existing_user = Users.query.filter_by(user_email=user_email).first()
        if existing_user:
            flash('Este email já existe')
            print('Este email já existe')
            return redirect(url_for('actions.register'))
        
        # Creating a new user and saving to the database
        new_user = Users(
            user_name=user_name,
            user_email=user_email,
            user_pwd_hash=user_pwd_hash,
            profession=user_profession
        )
        db.session.add(new_user)
        db.session.commit()
        
        # Logar o usuário automaticamente após o registro
        session['user_id'] = new_user.id
        session['user_name'] = new_user.user_name
        flash('Registro bem-sucedido e login automático realizado.')
        return redirect(url_for('views.dream_page'))  # Redirecionar para a página index
    except Exception as e:
        print(f'Erro de processo -> {e}')
    return render_template('signup.html')


@actions.route('/register_dream', methods=['POST'])
def register_and_analise_dream():
    if request.method == 'POST':
        dream = request.form['dream']
        
        llm = LLM()
        final_response_text_psicologic = llm.psicologic_analises(dream=dream)
        final_response_resume = llm.resume_analises(dream=dream)
        final_response_imaginary_gestions = llm.imaginary_sugestions(dream=dream)

        # Criando um novo objeto Dream e salvando no banco de dados
        new_dream = Dreams(
            user_original_text_dream=dream,
            llm_text_resume=final_response_resume,
            llm_psicologic_analisys=final_response_text_psicologic,
            llm_creative_sugestions=final_response_imaginary_gestions
        )
        db.session.add(new_dream)
        db.session.commit()
        
        return redirect(url_for('views.view_analysis', 
                                dream=dream, 
                                ai_analysis=final_response_text_psicologic, 
                                suggestions=markdown.markdown(final_response_imaginary_gestions)))
    return render_template('index.html')
