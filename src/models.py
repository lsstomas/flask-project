import mysql.connector
from mysql.connector import Error
from config import Config


class Produto:
    def __init__(self, nome, descricao, preco, id=None):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.preco = preco

    # Método para conectar ao banco de dados
    @staticmethod
    def get_db_connection():
        try:
            connection = mysql.connector.connect(
                host=Config.MYSQL_HOST,
                user=Config.MYSQL_USER,
                password=Config.MYSQL_PASSWORD,
                database=Config.MYSQL_DB,
                port=Config.MYSQL_PORT,
            )
            return connection
        except Error as e:
            print(f"Erro ao estabelecer conexão com a plataforma MySQL: {e}")
            return None

    # Método para listar todos produtos
    @staticmethod
    def get_all():
        connection = Produto.get_db_connection()

        if connection is not None:
            cursor = connection.cursor(dictionary=True)

            cursor.execute("SELECT * FROM produto")
            produtos = cursor.fetchall()

            cursor.close()
            connection.close()

            return produtos
        return []

    # Método para adicionar produtos
    def add_product(self):
        connection = Produto.get_db_connection()

        if connection is not None:
            cursor = connection.cursor()

            cursor.execute(
                f'INSERT INTO produto (nome, descricao, preco) VALUES ("{self.nome}", "{self.descricao}", {self.preco})'
            )

            connection.commit()
            cursor.close()
            connection.close()
