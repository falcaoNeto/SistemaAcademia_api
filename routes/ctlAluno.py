from flask import Blueprint, request
from models.aluno import Aluno
from models.endereco import Endereco

aluno_route = Blueprint('aluno', __name__)

@aluno_route.route('/CadastrarAluno', methods=['POST'])
def CadastrarAluno():
        matricula = request.form.get('matricula')
        nome = request.form.get('nome')
        data_nascimento = request.form.get('data_nascimento')
        cpf = request.form.get('cpf')
        email = request.form.get('email')
        telefone = request.form.get('telefone')
        logradouro = request.form.get('logradouro')
        cep = request.form.get('cep')
        rua = request.form.get('rua')
        num_casa = request.form.get('num_casa')
        bairro = request.form.get('bairro')
        cidade = request.form.get('cidade')

        endereco = Endereco(logradouro, cep, rua, num_casa, bairro, cidade)
        aluno = Aluno(matricula, nome, data_nascimento, cpf, email, telefone, id_endereco)

@aluno_route.route('/AtualizarAluno', methods=['PUT'])
def AtualizarAluno():
    matricula = request.form.get('matricula')
    nome = request.form.get('nome')
    data_nascimento = request.form.get('data_nascimento')
    cpf = request.form.get('cpf')
    email = request.form.get('email')
    telefone = request.form.get('telefone')

    aluno = Aluno(matricula, nome, data_nascimento, cpf, email, telefone)
    aluno.AtualizarAluno()


@aluno_route.route('/DeletarAluno', methods=['POST'])
def DeletarAluno():
    return 'DeletarAluno'

@aluno_route.route('/ListarAluno', methods=['POST'])
def ListarAluno():
    return 'ListarAluno'
