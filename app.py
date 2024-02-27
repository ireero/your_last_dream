from flask import Flask

app = Flask(__name__)

from views import views as views_blueprint

app.register_blueprint(views_blueprint)

if __name__ == '__main__':
    app.run()