# Dream

Dream Diary é uma aplicação Flask simples que permite aos usuários escreverem seus sonhos e armazená-los em um banco de dados SQLite. A aplicação inclui a data e a hora em que cada sonho foi registrado.

## Estrutura do Projeto

```plaintext
dream_diary/
│
├── app.py
├── models.py
├── views.py
├── templates/
│   └── index.html
├── static/
│   ├── css/
│   │   └── styles.css
│   └── js/
│       └── script.js
└── instance/
    └── dreams.db (será criado automaticamente)


## Instalação

1. Clone este repositório:
   ```sh
   git clone https://github.com/seu_usuario/dream_diary.git
   cd dream_diary

    Crie e ative um ambiente virtual:

    sh

python -m venv .venv
source .venv/bin/activate  # No Windows, use: .venv\Scripts\activate

Instale as dependências:

sh

    pip install flask flask_sqlalchemy

Uso

    Execute a aplicação:

    sh

    python app.py

    Acesse a aplicação no navegador em http://127.0.0.1:5000/.

    Use o formulário para inserir seus sonhos. A data e a hora serão registradas automaticamente.

Arquivos e Pastas

    app.py: Arquivo principal da aplicação Flask.
    models.py: Definição dos modelos de banco de dados.
    views.py: Definição das rotas e lógica de exibição.
    templates/: Contém os templates HTML.
    static/: Contém os arquivos CSS e JavaScript.
    instance/: Pasta onde o banco de dados SQLite será armazenado.

Modelo de Dados

A aplicação usa um modelo de dados simples com três campos:

    text_dream: O texto do sonho.
    date: A data em que o sonho foi registrado, no formato yyyymmdd.
    time: A hora em que o sonho foi registrado, no formato hh:mm.

Código Exemplo
app.py

python

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
from models import Dreams
from views import views

# Registrar o blueprint
app.register_blueprint(views)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Criar as tabelas no banco de dados
    app.run(debug=True)

models.py

python

from .app import db, app

class Dreams(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text_dream = db.Column(db.Text, nullable=False)
    date = db.Column(db.String(8), nullable=False)  # yyyymmdd
    time = db.Column(db.String(5), nullable=False)  # hh:mm

# Crie as tabelas no banco de dados
with app.app_context():
    db.create_all()

views.py

python

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

templates/index.html

html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Dream Diary</title>
    <link href="{{ url_for('static', filename='css/styles.css') }}" rel="stylesheet">
    <script src="{{ url_for('static', filename='js/script.js') }}" defer></script>
</head>
<body>
    <div class="container">
        <h1>Dream Diary</h1>
        <div class="date-block">
            <span id="current-date">{{ today_date }}</span>
        </div>
        <form action="/register_dream" method="post">
            <div class="form-group">
                <label for="dream">Write your dream:</label>
                <textarea id="dream" name="dream" rows="4" required></textarea>
            </div>
            <input type="submit" value="Submit">
        </form>
    </div>
</body>
</html>

static/css/styles.css

css

body {
    font-family: 'Roboto Slab', serif;
    background-color: #F8F8FF; /* Branco suave */
    color: #4B0082; /* Lavanda escura */
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}

.container {
    background-color: white;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    padding: 30px;
    max-width: 600px;
    width: 100%;
}

h1 {
    text-align: center;
    color: #4B0082; /* Lavanda escura */
    font-size: 2.5em;
    margin-bottom: 20px;
}

.date-block {
    text-align: center;
    margin-bottom: 20px;
    font-size: 1.2em;
    color: #4B0082; /* Lavanda escura */
}

label {
    font-weight: bold;
    color: #4B0082;
    display: block;
    margin-top: 10px;
}

textarea, input[type=submit] {
    width: 100%;
    padding: 14px;
    margin: 10px 0;
    box-sizing: border-box;
    border: 2px solid #4B0082; /* Borda lavanda escura */
    border-radius: 8px;
    font-size: 16px;
    font-family: 'Roboto Slab', serif;
}

input[type=submit] {
    background-color: #4B0082; /* Botão lavanda escura */
    color: white;
    cursor: pointer;
    transition: background-color 0.3s;
}

input[type=submit]:hover {
    background-color: #6A0DAD; /* Lavanda mais escura */
}

static/js/script.js

javascript

document.addEventListener('DOMContentLoaded', (event) => {
    // Você pode adicionar qualquer código JavaScript aqui se necessário no futuro
});
