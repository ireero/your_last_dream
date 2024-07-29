from .app import db, app
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import UniqueConstraint
from datetime import datetime

class BaseModel(db.Model):
    __abstract__ = True
    date_created = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    date_modified = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

class Dreams(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    user_original_text_dream = db.Column(db.Text, nullable=False)
    llm_text_resume = db.Column(db.Text, nullable=False)
    llm_psicologic_analisys = db.Column(db.Text, nullable=False)
    llm_creative_sugestions = db.Column(db.Text, nullable=False)

class Users(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), nullable=False)
    user_email = db.Column(db.String(100), nullable=False, unique=True, index=True)
    user_pwd_hash = db.Column(db.String(128), nullable=False)
    profession = db.Column(db.String(50), nullable=False)  # Novo campo

    def set_password(self, password):
        self.user_pwd_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.user_pwd_hash, password)

    __table_args__ = (UniqueConstraint('user_email', name='_user_email_uc'),)

# Criação do banco de dados e tabelas
with app.app_context():
    db.create_all()
