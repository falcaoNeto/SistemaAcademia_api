from BD.bd import engine
from dataclasses import dataclass
from sqlalchemy.orm import sessionmaker
from models.funcionario import Funcionario

@dataclass
class Instrutor(Funcionario):
    funcionario_nit: int
    grau_academico: str