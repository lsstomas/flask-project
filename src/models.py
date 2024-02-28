from src import db
from werkzeug.security import generate_password_hash, check_password_hash


class Produto(db.Model):
    __tablename__ = "produto"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(200), nullable=True)
    preco = db.Column(db.Float, nullable=False)

    def __init__(self, nome, email, senha) -> None:
        self.nome = nome
        self.email = email
        self.senha = senha

    def __repr__(self) -> str:
        return f"ID: {self.id} | Produto: {self.nome}"


class Usuario(db.Model):
    __tablename__ = "usuario"
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    senha = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.senha = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.senha, password)

    def __init__(self, usuario, email, senha) -> None:
        self.usuario = usuario
        self.email = email
        self.set_password(senha)

    def __repr__(self) -> str:
        return f"Usuário: {self.usuario}"
