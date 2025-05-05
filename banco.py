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

    def getAllAlunos(self) -> list:
        self.connect()
        self.cursor.execute("select * from alunos")
        alunos = [
            {"matricula": row[0], "nome": row[1], "ano": row[2]}
            for row in self.cursor.fetchall()
        ]
        self.close()
        return alunos

    def getAluno(self, matricula: int) -> dict:
        self.connect()
        self.cursor.execute(
            f"select * from alunos where matricula={matricula}"
        )
        alunos = [
            {"matricula": row[0], "nome": row[1], "ano": row[2]}
            for row in self.cursor.fetchall()
        ]
        self.close()
        try:
            return True, alunos[0]
        except IndexError:
            return False, "Aluno não encontrado"

    def getAlunos(self, disciplina: int) -> list:
        self.connect()
        self.cursor.execute(
            f"select * from materias where codigo={disciplina}"
        )
        materia = [
            {"codigo": row[0], "nome": row[1], "carga": row[2]}
            for row in self.cursor.fetchall()
        ]
        try:
            materia[0]
        except IndexError:
            return False, "Disciplina não encontrado"
        self.cursor.execute(
            f"select * from notas where materia='{materia[0]['nome']}'"
        )
        alunos = self.cursor.fetchall()
        lista = []
        for i in alunos:
            x, y = self.getAluno(i[1])
            lista.append(y)
        self.close()
        try:
            lista[0]
            return True, lista
        except IndexError:
            return False, "Nenhum aluno não encontrado"

    def getSemestre(self, matricula: int, semestre: int):
        pass

    def addAluno(self, name, matricula, ano=2025):
        self.connect()
        self.cursor.execute('INSERT INTO alunos (matricula, nome, ano) VALUES (?,?,?)', (name, matricula, ano))
        self.connection.commit()
        self.close()

