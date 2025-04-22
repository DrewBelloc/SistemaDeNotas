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

    def getAluno(self, matricula: int):
        self.connect()
        if matricula == 0:
            self.cursor.execute("select * from alunos")
            alunos = [
                {"matricula": row[0], "nome": row[1], "ano": row[2]}
                for row in self.cursor.fetchall()
            ]
            return alunos
        else:
            self.cursor.execute(
                f"select * from alunos where matricula={matricula}"
            )
            alunos = [
                {"matricula": row[0], "nome": row[1], "ano": row[2]}
                for row in self.cursor.fetchall()
            ]
            return alunos[0]
