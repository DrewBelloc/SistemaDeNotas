import sqlite3

class Banco:
    connection = None
    cursor = None

    def __init__(self):
        try:
            self.connect()
            print("Conexão com o banco realizada com sucesso!")
        except Exception as error:
            print(f"Erro ao conectar no banco: {error}")

    def connect(self):
        self.connection = sqlite3.connect('banco.db')
        self.cursor = self.connection.cursor()

    def close(self):
        if self.connection:
            self.connection.close()

    def getAluno(int: matricula):
        pass
