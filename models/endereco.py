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

    def CadastrarEndereco(self):
        try:
            sessionLocal = sessionmaker(bind=engine)
            session = sessionLocal()
            session.execute(f'INSERT INTO endereco (logradouro, cep, rua, num_casa, bairro, cidade)
            VALUES ("{self.logradouro}", "{self.cep}", "{self.rua}", "{self.num_casa}", "{self.bairro}", "{self.cidade}")')
            session.commit()
            return True
        except:
            return False
        finally:
            session.close()