from flask import Blueprint, request
from models.adm import Adm
from models.endereco import Endereco

adm_route = Blueprint('adm', __name__)

@adm_route.route('/CadastrarAdm', methods=['POST'])
def CadastrarAdm():
    data = request.get_json()
    logradouro = data.get('logradouro')
    cep = data.get('cep')
    rua = data.get('rua')
    num_casa = data.get('num_casa')
    bairro = data.get('bairro')
    cidade = data.get('cidade')
    endereco = Endereco(logradouro, cep, rua, num_casa, bairro, cidade)
    id_endereco = endereco.CadastrarEndereco()

    if id_endereco:
        nit = data.get('nit')
        nome = data.get('nome')
        data_nascimento = data.get('data_nascimento')
        cpf = data.get('cpf')
        email = data.get('email')
        telefone = data.get('telefone')
        token = data.get('token')
        adm = Adm(nit, nome, data_nascimento, cpf, email, telefone, id_endereco, token)
        result = adm.CadastrarAdm()
        if result:
            return {"mensagem": "Adm cadastrado com sucesso!"}, 201
        return {"mensagem": "Erro ao cadastrar administrador"}, 404
    
    return {"mensagem": "Erro ao cadastrar endereco"}, 404