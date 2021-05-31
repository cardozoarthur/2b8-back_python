from Grupo4 import db
import datetime as dt

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cpf = db.Column(db.String(80), unique=True, nullable=True)
    senha = db.Column(db.String(120), nullable=False)
    idade = db.Column(db.Integer, nullable=True)
    cep = db.Column(db.Integer, nullable=True)
    telefone = db.Column(db.Integer, nullable=True)
    email = db.Column(db.String(120), nullable=True)
    sexo = db.Column(db.String(120), nullable=True)
    cidade = db.Column(db.String(120), nullable=False)
    bairro = db.Column(db.String(120), nullable=True)
    permissao = db.Column(db.String(120), nullable=False, default='cpf')

    def __repr__(self):
        return '<User %r>' % self.cpf

class Pesquisa(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    cidade = db.Column(db.String(80), nullable=False)
    cardiopatia = db.Column(db.Integer)
    diabetes = db.Column(db.Integer)
    pressao_alta = db.Column(db.Integer)
    cancer = db.Column(db.Integer)
    hiv = db.Column(db.Integer)
    obesidade = db.Column(db.Integer)
    problemas_renais = db.Column(db.Integer)
    sifilis = db.Column(db.Integer)
    hepatite = db.Column(db.Integer)
    tuberculose = db.Column(db.Integer)

    febre = db.Column(db.Integer)
    tosse = db.Column(db.Integer)
    dor_garganta = db.Column(db.Integer)
    dificuldade_respirar = db.Column(db.Integer)
    dor_cabeca = db.Column(db.Integer)
    dor_peito = db.Column(db.Integer)
    nausea = db.Column(db.Integer)
    coriza = db.Column(db.Integer)
    fadiga = db.Column(db.Integer)
    dor_olhos = db.Column(db.Integer)
    perda_paladar = db.Column(db.Integer)
    dor_muscular = db.Column(db.Integer)

    data = db.Column(db.Date, default=dt.datetime.now())