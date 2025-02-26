from BD.bd import engine
from dataclasses import dataclass
from sqlalchemy.orm import sessionmaker
from models.funcionario import Funcionario

@dataclass
class Administrador(Funcionario):
    funcionario_nit: int
    token: str