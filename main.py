from flask import Flask
from routes.aluno_route import aluno_route
from routes.home_route import home_route
app = Flask(__name__)

app.register_blueprint(aluno_route)
app.register_blueprint(home_route)


if __name__ == '__main__':
    app.run(debug=True)