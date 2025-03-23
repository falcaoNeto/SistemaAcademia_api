from BD.bd import engine
from dataclasses import dataclass
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
from typing import Optional
from werkzeug.security import generate_password_hash

@dataclass
class Login:
    username: str
    password: str
    is_adm: Optional[bool] = None


    def Auth(self):
        try:
            sessionLocal = sessionmaker(bind=engine)
            session = sessionLocal()
            query = text("""SELECT * FROM mydb.usuario WHERE username = :username""")
            params = {
                "username": self.username
            }
            result = session.execute(query, params)
            user = result.fetchone()
            session.commit()
            return user
        except Exception as e:
            return str(e)
        finally:
            session.close()


    def CadastrarUser(self):
        try:
            sessionLocal = sessionmaker(bind=engine)
            session = sessionLocal()
            query = text("""
            INSERT INTO mydb.usuario (username, senha_hash, is_admin)
            VALUES (:username, :password, :is_adm)
            RETURNING id_usuario
            """)
            params = {
                "username": self.username,
                "password":  generate_password_hash(self.password, method='pbkdf2:sha256'),
                "is_adm": self.is_adm
            }
            result = session.execute(query, params)
            id_usuario = result.fetchone()[0]
            session.commit()
            if id_usuario:
                return id_usuario
            return False
        except Exception as e:
            print(f"Erro: {e}")
            session.rollback()
            return False
        finally:
            session.close()