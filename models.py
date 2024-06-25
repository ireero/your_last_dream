from .app import db, app

class Dreams(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text_dream = db.Column(db.Text, nullable=False)
    date = db.Column(db.String(8), nullable=False)  # yyyymmdd
    time = db.Column(db.String(5), nullable=False)  # hh:mm

# Crie as tabelas no banco de dados
with app.app_context():
    db.create_all()
