from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, redirect, render_template
from flask_cors import CORS, cross_origin
import datetime as dt
import json
from hashlib import md5

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

from Grupo4.models import User, Pesquisa
from Grupo4 import apiconnection
from Grupo4 import errorhandling as eh

#rota para teste sem o front end em react
@app.route("/")
def displayHome():
    return render_template('pesquisa_form.html')
    #return render_template('login.html')
    return render_template('form.html')

#rotas normais
@app.route("/dashboard/<cidade>")
@cross_origin()
def displayDashboard(cidade):
    legenda = ['Fev', 'Mar', 'Abr', 'Mai']
    valores = [11390, 13290, 15032, 18332]
    dict = {'mortes': {'valores': valores, 'legenda': legenda}, 'novos_casos': {'valores':[68731, 73905, 81532, 88362], 'legenda': legenda}}
    return json.dumps(dict)

@app.route("/cadastro", methods=['POST'])
@cross_origin()
def createUser():
    if request.method == 'POST':
        cpf = request.form['cpf']
        senha = request.form['senha']
        idade = request.form['idade']
        cep = request.form['cep']
        cidade = request.form['cidade']
        bairro = request.form['bairro']

        #validateFields()

        new_user = User(cpf=cpf, senha=senha, idade=idade, cep=cep, cidade=cidade, bairro=bairro)
        db.session.add(new_user)
        db.session.commit()
        for each in User.query.filter_by(cpf=cpf, senha=senha):
            dict = lambda r: {c.name: str(getattr(r, c.name)) for c in r.__table__.columns}
        return json.dumps(dict(each), ensure_ascii=False)
    else:
        return eh.e405()

@app.route("/cadastro-prefeitura", methods=['POST'])
@cross_origin()
def createPrefeituraUser():
    if request.method == 'POST':
        senha = request.form['senha']
        cidade = request.form['cidade']
        telefone = request.form['telefone']
        email = request.form['email']

        #validateFields()

        new_user = User(senha=senha, email=email, telefone=telefone, cidade=cidade, permissao='prefeitura')
        db.session.add(new_user)
        db.session.commit()
        for each in User.query.filter_by(email=email, senha=senha):
            dict = lambda r: {c.name: str(getattr(r, c.name)) for c in r.__table__.columns}
        return json.dumps(dict(each), ensure_ascii=False)
    else:
        return eh.e405()

@app.route("/login", methods=['POST'])
@cross_origin()
def logUser():
    if request.method == 'POST':
        cpf = request.form['cpf']
        senha = request.form['senha']
        user = User.query.filter_by(cpf=cpf).first()
        if user and user.senha == senha:
            for each in User.query.filter_by(cpf=cpf, senha=senha):
                dict = lambda r: {c.name: str(getattr(r, c.name)) for c in r.__table__.columns}
            return json.dumps(dict(each), ensure_ascii=False)
        else:
            return eh.e401()
    else:
        return eh.e405()

@app.route("/pesquisa", methods=['POST'])
@cross_origin()
def createPesquisa():
    if request.method == 'POST':
        raw_data = request.form.to_dict()
        dados = {}
        for k, v in raw_data.items():
            try:
                dados[k] = int(v)
            except:
                dados[k] = v
        #validateFields()
        nova_pesquisa = Pesquisa(**dados)
        db.session.add(nova_pesquisa)
        try:
            db.session.commit()
            return json.dumps({"code": 200,
                       "description": "sucesso"}, ensure_ascii=False)
        except TypeError as e:
            return eh.e500(msg=e)
    else:
        return eh.e405()

@app.route("/pesquisa/<cidade>", methods=['GET', 'POST'])
@cross_origin()

def showPesquisas(cidade):
    if request.method == 'GET':
        print('cidade: ', cidade)
        query = Pesquisa.query.filter_by(cidade=cidade).all()
        response = {}
        list = []
        for each in query:
            dict = lambda r: {c.name: str(getattr(r, c.name)) for c in r.__table__.columns}
            list.append(dict(each))
        response['pesquisas'] = list
        return json.dumps(response)

    else:
        return eh.e405()

def validateFields(fields_list):
    pass

def runMatlabCode(file):
    pass

def objectToDict(obj):
    return