from flask import Blueprint, render_template, request, redirect, url_for
from .app import db
from .models import Dreams
from datetime import datetime

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def index():
    # today_date = datetime.today().strftime('%d/%m/%Y')
    print('aqui')
    return render_template('login.html')

@views.route('/dream')
def dream_page():
    return render_template('index.html')

@views.route('/view_analysis')
def view_analysis():
    dream = request.args.get('dream')
    ai_analysis = request.args.get('ai_analysis')
    suggestions = request.args.get('suggestions')
    
    return render_template('views.html', dream=dream, ai_analysis=ai_analysis, suggestions=suggestions)