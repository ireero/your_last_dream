from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Criação do diretório instance se não existir
if not os.path.exists(os.path.join(os.getcwd(), 'instance')):
    os.makedirs(os.path.join(os.getcwd(), 'instance'))

# Configuração do SQLAlchemy para usar o banco de dados na pasta instance
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.getcwd(), 'instance', 'dreams.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicialização do SQLAlchemy
db = SQLAlchemy(app)

# Importar modelos e blueprints
from .views import views

# Registrar o blueprint
app.register_blueprint(views)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Criar as tabelas no banco de dados
    app.run(debug=True)
