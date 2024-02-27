from app import db

class Dreams(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text_dream = db.Column(db.Text, nullable=False)