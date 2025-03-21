from flask import Blueprint, request, jsonify
from models.aluno import Aluno
from models.endereco import Endereco


aluno_route = Blueprint('aluno', __name__)


@aluno_route.route('/FormCadastrarAluno', methods=['GET'])
def FormCadastrarAluno():
    ...

@aluno_route.route('/CadastrarAluno', methods=['POST'])
def CadastrarAluno():
    data = request.get_json()  # Obtém o JSON enviado
    matricula = data.get('matricula')
    nome = data.get('nome')
    data_nascimento = data.get('data_nascimento')
    cpf = data.get('cpf')
    email = data.get('email')
    telefone = data.get('telefone')
    logradouro = data.get('logradouro')
    cep = data.get('cep')
    rua = data.get('rua')
    num_casa = data.get('num_casa')
    bairro = data.get('bairro')
    cidade = data.get('cidade')
    plano_id = data.get('plano_id')

    endereco = Endereco(logradouro, cep, rua, num_casa, bairro, cidade)
    id_end = endereco.CadastrarEndereco()

    aluno = Aluno(matricula, nome, data_nascimento, cpf, email, telefone, id_end, plano_id)
    result = aluno.CadastrarAluno()

    if result:
        return jsonify({"mensagem": "Aluno cadastrado com sucesso!", "dados": data}), 201
    
    return jsonify({"mensagem": "error!", "dados": id_end}), 404


@aluno_route.route('/ListarAluno', methods=['GET'])
def ListarAluno():
    aluno = Aluno(0, "", "", "", "", "", 0, 0)
    result = aluno.ListarAluno()
    if result:
        alunos = [
            {"matricula": row[0], "nome": row[1], "data_nascimento": row[2], "cpf": row[3], "email": row[4], "telefone": row[5], "endereco_id": row[6], "plano_id": row[7]}
            for row in result
        ]
        return jsonify({"alunos": alunos}), 200
    return jsonify({"mensagem": "Erro ao listar alunos"}), 404



@aluno_route.route('/FormAtualizarAluno/<int:matricula>', methods=['GET'])
def FormAtualizarAluno(matricula):
    aluno = Aluno(0, "", "", "", "", "", 0, 0)
    resultAluno = aluno.GetAluno(matricula)
    if resultAluno:
        result = resultAluno[0]
        endereco = Endereco(0, "", "", 0, "", "")
        print(type(result[6]))
        result_endereco = endereco.GetEndereco(result[6])
        if result_endereco:
            result_endereco = result_endereco[0]
            aluno = {"matricula": result[0], "nome": result[1], "data_nascimento": result[2], "cpf": result[3],
            "email": result[4], "telefone": result[5], "endereco_id": result[6],
            "plano_id": result[7], "logradouro": result_endereco[1], "cep": result_endereco[2],
            "rua": result_endereco[3], "num_casa": result_endereco[4], "bairro": result_endereco[5], "cidade": result_endereco[6]}
            return jsonify({"aluno": aluno}), 200
        
        return jsonify({"mensagem": "Error ao selecionar endereco"}), 404

    return jsonify({"mensagem": "Error ao selecionar aluno"}), 404



@aluno_route.route('/FormAtualizarAlunoAula', methods=['GET'])
    


@aluno_route.route('/AtualizarAluno', methods=['PUT'])
def AtualizarAluno():
    data = request.get_json()
    matricula = data.get('matricula')
    nome = data.get('nome')
    data_nascimento = data.get('data_nascimento')
    cpf = data.get('cpf')
    email = data.get('email')
    telefone = data.get('telefone')
    plano_id = data.get('plano_id')
    aluno = Aluno(matricula, nome, data_nascimento, cpf, email, telefone, 0, plano_id)
    result = aluno.AtualizarAluno()
    if result:
        return jsonify({"mensagem": "Aluno atualizado com sucesso!"}), 200
    return jsonify({"mensagem": "Erro ao atualizar aluno"}), 404