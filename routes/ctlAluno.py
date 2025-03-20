from dataclasses import dataclass
from BD.bd import engine
from sqlalchemy.orm import sessionmaker

@dataclass
class Aluno:
    matricula: int
    nome: str
    data_nascimento: str
    cpf: str
    email: str
    telefone: str
    id_endereco: int

    def CadastrarAluno(self):
        try:
            SessionLocal = sessionmaker(bind=engine)
            session = SessionLocal()
            session.execute(f'INSERT INTO Aluno (matricula, nome, data_nascimento, cpf, email, telefone)
            VALUES ({self.matricula}, "{self.nome}", "{self.data_nascimento}", "{self.cpf}", "{self.email}", "{self.telefone}", "{self.id_endereco}")
            Returning id_endereco')
            id_endereco = session.scalar()
            session.commit()
            return id_endereco
        except:
            return False
        finally:
            session.close()


    def AtualizarAluno(self):
        try:
            SessionLocal = sessionmaker(bind=engine)
            session = SessionLocal()
            session.execute(f'UPDATE Aluno SET
            nome = "{self.nome}", data_nascimento = "{self.data_nascimento}", 
            cpf = "{self.cpf}", email = "{self.email}", telefone = "{self.telefone}" WHERE id_aluno = {self.matricula}')
            session.commit()
            return True
        except:
            return False
        finally:
            session.close()
            

    def ExcluirAluno(self, matricula):
        try:
            SessionLocal = sessionmaker(bind=engine)
            session = SessionLocal()
            session.execute(f'DELETE FROM Aluno WHERE id_aluno = {matricula}')
            session.commit()
            return True
        except:
            return False
        finally:
            session.close()
            