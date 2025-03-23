from dataclasses import dataclass
from models.funcionario import Funcionario
from sqlalchemy.sql import text

@dataclass
class Instrutor(Funcionario):
    grau_academico: str

    def CadastrarInstrutor(self, session):
        query_funcionario = text("""
        INSERT INTO mydb.funcionario (NIT, nome, data_nascimento, cpf, email, telefone, endereco_id_endereco, usuario_id_usuario)
        VALUES (:NIT, :nome, :data_nascimento, :cpf, :email, :telefone, :endereco_id_endereco, :id_usuario)
        """)
        params_funcionario = {
            "NIT": self.nit,
            "nome": self.nome,
            "data_nascimento": self.data_nascimento,
            "cpf": self.cpf,
            "email": self.email,
            "telefone": self.telefone,
            "endereco_id_endereco": self.id_endereco,
            "id_usuario": self.id_usuario
        }
        session.execute(query_funcionario, params_funcionario)
        query_instrutor = text("""
        INSERT INTO mydb.instrutor (funcionario_NIT, grau_academico)
        VALUES (:funcionario_NIT, :grau_academico)
        """)
        params_instrutor = {
            "funcionario_NIT": self.nit,
            "grau_academico": self.grau_academico
        }
        session.execute(query_instrutor, params_instrutor)
        