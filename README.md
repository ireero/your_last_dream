
# Nap

Nap é uma aplicação web para análise de sonhos que utiliza inteligência artificial para fornecer resumos, análises psicológicas e sugestões criativas baseadas nos sonhos dos usuários. A aplicação permite que os usuários se registrem, façam login e submetam seus sonhos para análise.

## Funcionalidades

- **Registro de Usuário**: Permite que novos usuários se registrem com nome de usuário, email, senha e profissão.
- **Login de Usuário**: Autenticação de usuários registrados.
- **Análise de Sonhos**: Usuários podem registrar seus sonhos e receber uma análise detalhada utilizando inteligência artificial.
- **Resumos de Sonhos**: Geração de resumos dos sonhos submetidos.
- **Sugestões Criativas**: Fornecimento de sugestões criativas baseadas nos sonhos dos usuários.

## Tecnologias Utilizadas

- **Flask**: Framework web para Python.
- **SQLAlchemy**: ORM para gerenciamento do banco de dados.
- **Werkzeug**: Biblioteca para hashing de senhas e segurança.
- **Flask-Migrate**: Extensão para gerenciamento de migrações de banco de dados.
- **Markdown**: Utilizado para renderizar sugestões criativas em formato markdown.

## Instalação

### Pré-requisitos

- Python 3.7 ou superior
- Pip (gerenciador de pacotes do Python)

### Passos para Instalação

1. Clone o repositório:

```sh
git clone https://github.com/seu-usuario/nap.git
cd nap
```

2. Crie um ambiente virtual:

```sh
python -m venv venv
```

3. Ative o ambiente virtual:

- Windows:
    ```sh
    venv\Scripts\activate
    ```
- Linux/Mac:
    ```sh
    source venv/bin/activate
    ```

4. Instale as dependências:

```sh
pip install -r requirements.txt
```

5. Configure as variáveis de ambiente:

- Crie um arquivo `.env` na raiz do projeto e adicione as seguintes linhas:

    ```env
    FLASK_APP=run.py
    FLASK_ENV=development
    SECRET_KEY=your_secret_key
    SQLALCHEMY_DATABASE_URI=sqlite:///app.db
    ```

6. Inicialize o banco de dados:

```sh
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```

7. Execute a aplicação:

```sh
flask run
```

## Uso

### Registro de Usuário

1. Acesse `http://127.0.0.1:5000/register` no seu navegador.
2. Preencha o formulário de registro com seu nome de usuário, email, senha e profissão.
3. Clique em "Cadastrar" para registrar um novo usuário.

### Login de Usuário

1. Acesse `http://127.0.0.1:5000/login` no seu navegador.
2. Preencha o formulário de login com seu nome de usuário e senha.
3. Clique em "Login" para autenticar.

### Análise de Sonhos

1. Após fazer login, você será redirecionado para a página principal.
2. Submeta seu sonho para análise preenchendo o formulário e clicando em "Enviar".

## Estrutura do Projeto

```plaintext
nap/
├── app.py
├── models.py
├── actions.py
├── llm.py
├── requirements.txt
├── .env
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── signup.html
│   ├── view_analysis.html
├── static/
│   ├── css/
│   │   ├── views.css
│   │   ├── signup.css
│   ├── js/
│   │   ├── scripts_signup.js
│   ├── images/
│   │   ├── logo_nap.png
│   │   ├── nuvem.png
└── migrations/
```
