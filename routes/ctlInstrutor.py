from flask import Blueprint, request
from models.instrutor import Instrutor
from models.endereco import Endereco

instrutor_route = Blueprint('instrutor', __name__)

@instrutor_route.route('/FormCadastrarInstrutor', methods=['GET'])
def FormCadastrarInstrutor():
    return {"mensagem": "Formulário de cadastro de instrutor"}

@instrutor_route.route('/CadastrarInstrutor', methods=['POST'])
def CadastrarInstrutor():
    data = request.get_json()
    logradouro = data.get('logradouro')
    cep = data.get('cep')
    rua = data.get('rua')
    num_casa = data.get('num_casa')
    bairro = data.get('bairro')
    cidade = data.get('cidade')
    endereco = Endereco(logradouro, cep, rua, num_casa, bairro, cidade)
    id_endereco = endereco.CadastrarEndereco()

    user = data.get('user')
    passwd = data.get('passwd')
    login1 = Login()
    login1.user = user
    login1.password = passwd
    login1.is_adm = True
    login1.CadastrarUser()

    if id_endereco:
        nit = data.get('nit')
        nome = data.get('nome')
        data_nascimento = data.get('data_nascimento')
        cpf = data.get('cpf')
        email = data.get('email')
        telefone = data.get('telefone')
        grau_academico = data.get('grau_academico')
        instrutor = Instrutor(nit, nome, data_nascimento, cpf, email, telefone, id_endereco, grau_academico)
        result = instrutor.CadastrarInstrutor()
        if result:
            return {"mensagem": "Instrutor cadastrado com sucesso!"}, 201
        return {"mensagem": "Erro ao cadastrar instrutor"}, 404
    
    return {"mensagem": "Erro ao cadastrar endereco"}, 404
