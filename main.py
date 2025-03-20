from flask import Flask, request, jsonify, session
#from routes.ctlAluno import aluno_route
from routes.Auth import auth
from flask_cors import CORS
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

app.secret_key = os.getenv("SECRET_KEY")
CORS(app, supports_credentials=True)

app.register_blueprint(auth)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
