from flask import Blueprint, render_template, request, redirect, url_for
from .app import db
from .models import Dreams
from datetime import datetime

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def index():
    today_date = datetime.today().strftime('%d-%m-%Y')
    return render_template('index.html', today_date=today_date)

@views.route('/register_dream', methods=['POST'])
def register_dream():
    if request.method == 'POST':
        dream = request.form['dream']
        date = datetime.now().strftime('%Y%m%d')
        time = datetime.now().strftime('%H:%M')
        new_dream = Dreams(text_dream=dream, date=date, time=time)
        db.session.add(new_dream)
        db.session.commit()
        return redirect(url_for('views.index'))
    today_date = datetime.today().strftime('%Y-%m-%d')
    return render_template('index.html', today_date=today_date)
