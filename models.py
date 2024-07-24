from .app import db, app

class Dreams(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_original_text_dream = db.Column(db.Text, nullable=False)
    llm_text_resume = db.Column(db.Text, nullable=False)
    llm_psicologic_analisys = db.Column(db.Text, nullable=False)
    llm_creative_sugestions = db.Column(db.Text, nullable=False)
    date = db.Column(db.String(8), nullable=False)  # yyyymmdd
    time = db.Column(db.String(5), nullable=False)  # hh:mm

with app.app_context():
    db.create_all()
