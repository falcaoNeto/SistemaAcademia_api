from dataclasses import dataclass

@dataclass
class Aluno:
    matricula: int
    nome: str
    data_nascimento: str
    cpf: str
    email: str
    telefone: str
    id_endereco: int