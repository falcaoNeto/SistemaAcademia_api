from dataclasses import dataclass
from models.funcionario import Funcionario

@dataclass
class Administrador(Funcionario):
    funcionario_nit: int
    token: str