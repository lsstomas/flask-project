import mysql.connector
from config import Config


class Produto:
    def __init__(self, id, nome, descricao, preco):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.preco = preco

    # Método para conectar ao banco de dados
    @staticmethod
    def get_db_connection():
        return mysql.connector.connect(
            host=Config.MYSQL_HOST,
            port=Config.MYSQL_PORT,
            user=Config.MYSQL_USER,
            password=Config.MYSQL_PASSWORD,
            database=Config.MYSQL_DB,
        )

    # Método para listar todos produtos
    @staticmethod
    def get_all():
        connection = Produto.get_db_connection()

        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM produto")

        produtos = cursor.fetchall()

        cursor.close()
        connection.close()

        return produtos
