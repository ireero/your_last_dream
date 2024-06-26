from flask import Blueprint, render_template, request, redirect, url_for
from .app import db
from .models import Dreams
from datetime import datetime

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def index():
    today_date = datetime.today().strftime('%d/%m/%Y')
    return render_template('index.html', today_date=today_date)
