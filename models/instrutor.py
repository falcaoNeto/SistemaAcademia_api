from dataclasses import dataclass
from models.funcionario import Funcionario

@dataclass
class Instrutor(Funcionario):
    funcionario_nit: int
    grau_academico: str