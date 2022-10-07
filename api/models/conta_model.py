from api import db

class Conta(db.Model):
    __tablename__='conta'

    id = db.Column(db.Interger, primary_key=True, autoincrement=True, nullable=False)
    nome = db.Column(db.String(50), nullable=False)
    resumo = db.Column(db.String(150), nullable=False)
    valor = db.Column(db.Float, nullable=False)