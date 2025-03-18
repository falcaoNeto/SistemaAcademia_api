from BD.bd import engine
from dataclasses import dataclass
from sqlalchemy.orm import sessionmaker

@dataclass
class Endereco:
    logradouro: str
    cep: str
    rua: str
    num_casa: int
    bairro: str
    cidade: str 