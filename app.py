from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dreams.db'
db = SQLAlchemy(app)

from views import views as views_blueprint

app.register_blueprint(views_blueprint)

if __name__ == '__main__':
    app.run()