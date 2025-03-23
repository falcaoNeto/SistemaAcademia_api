from dataclasses import dataclass

@dataclass
class Funcionario:
    nit: int
    nome: str
    data_nascimento: str
    cpf: str
    email: str
    telefone: str
    id_endereco: int
    id_usuario: int