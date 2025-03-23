from flask import Blueprint, request, jsonify, session
from werkzeug.security import check_password_hash
from models.login import Login


login_route = Blueprint('login', __name__)



@login_route.route('/FormLogin', methods=['GET'])
def FormLogin():
    return {"mensagem": "Formulário de login"}




@login_route.route('/LoginUser', methods=['POST'])
def LoginUser():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    is_adm = data.get('is_adm')

    teste = Login(username, password)
    user = teste.Auth()

    if user:
        if check_password_hash(user[3], password):
            session['adm'] = username
            session['is_adm'] = is_adm
            return jsonify({'reponse': 'usuario logado'}), 200
        
        return jsonify({'reponse': 'senha incorreta'}), 401

    return jsonify({'reponse': 'usuario não encontrado'}), 404











    
@login_route.route('/session', methods=['GET'])
def get_session():
    user = session.get('user')
    if user:
        return jsonify({'permission':'OK'}), 200
    return jsonify({'permission': 'ERR'}), 401 