'''
Brasília 2019 - UNB
Criado em  25/10/2019
por Ingrid, Michel, Ronald, Victor

API REST com propósito de priorização utilizando algoritmos de busca e ordenação HEAP a nível de aplicação 

'''
# ------- Config virtual env------
#$  pip install virtualenv
#$ virtualenv venv
#$ source venv/bin/activate
#$ pip install flask flask-jsonpify flask-sqlalchemy flask-restful

from flask import Flask

app = Flask(__name__)

from app.controllers import server_ctrl
