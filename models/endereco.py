from dataclasses import dataclass
from sqlalchemy.sql import text

@dataclass
class Endereco:
    logradouro: str
    cep: str
    rua: str
    num_casa: int
    bairro: str
    cidade: str

    def CadastrarEndereco(self, session):
        query = text("""INSERT INTO mydb.endereco (logradouro, cep, rua, num_casa, bairro, cidade)
                        VALUES (:logradouro, :cep, :rua, :num_casa, :bairro, :cidade)
                        RETURNING id_endereco""")
        params = {
            "logradouro": self.logradouro,
            "cep": self.cep,
            "rua": self.rua,
            "num_casa": self.num_casa,
            "bairro": self.bairro,
            "cidade": self.cidade
        }
        result = session.execute(query, params)
        id_endereco = result.fetchone()[0]
        return id_endereco
    
    def GetEndereco(self, id_endereco, session):
        query = text("""SELECT * FROM mydb.endereco WHERE id_endereco = :id_endereco""")
        params = {
            "id_endereco": id_endereco
        }
        result = session.execute(query, params)
        endereco = result.fetchone()
        print(endereco)
        return endereco

