from flask import Blueprint, request
from models.instrutor import Instrutor

instrutor_route = Blueprint('instrutor', __name__)

@instrutor_route.route('/CadastrarInstrutor', methods=['POST'])
def CadastrarInstrutor():
    nit = request.form.get('nit')
    nome = request.form.get('nome')
    data_nascimento = request.form.get('data_nascimento')
    cpf = request.form.get('cpf')
    email = request.form.get('email')
    telefone = request.form.get('telefone')
    grau_academico = request.form.get('grau_academico')

    instrutor = Instrutor(nit, grau_academico)
    instrutor.CadastrarInstrutor()