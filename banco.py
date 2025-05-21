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

    def getSemestre(self, matricula: str, semestre: int) -> list:
        self.connect()
        self.cursor.execute(
            f"select * from notas where aluno = {matricula} and periodo = {semestre}"
            )
        
        notas = [
            {
                "materia": row[0],
                "aluno": row[1], 
                "periodo": row[2],
                "sim1": row[3],
                "sim2": row[4],
                "av": row[5],
                "avs": row[6]
            }
            for row in self.cursor.fetchall()
        ]
        self.close()
        return notas

    def addAluno(self, name, matricula, ano=2025):
        self.connect()
        self.cursor.execute('INSERT INTO alunos (matricula, nome, ano) VALUES (?,?,?)', (name, matricula, ano))
        self.connection.commit()
        self.close()

    def updateNome(self, matricula, new_name):
        state, aluno = self.getAluno(matricula)
        if not aluno:
            self.close()
            return False, "Aluno não encontrado"

        if aluno['nome'] == new_name:
            self.close()
            return False, "O novo nome é igual ao atual"

        self.connect()
        self.cursor.execute('UPDATE alunos SET nome = ? WHERE matricula = ?', (new_name, matricula))
        self.connection.commit()

        state, aluno_atualizado = self.getAluno(matricula)
        if aluno_atualizado['nome'] == new_name:
            self.close()
            return True, aluno_atualizado
        else:
            self.close()
            return False, "Falha ao atualizar o nome"

    def getAllDisciplinas(self, matricula: str) -> list:
        self.connect()
        self.cursor.execute(
            "SELECT materia FROM notas WHERE aluno=?", (matricula,)
        )
        materias_notas = [row[0] for row in self.cursor.fetchall()]

        disciplinas = []
        for materia_nome in materias_notas:
            self.cursor.execute(
                "SELECT * FROM materias WHERE nome=?", (materia_nome,)
            )
            materia = self.cursor.fetchone()
            if materia:
                disciplinas.append({
                    "codigo": materia[0],
                    "nome": materia[1],
                    "carga": materia[2]
                })

        self.close()
        return disciplinas
    def getAllProfessores(self) -> list:
        self.connect()
        self.cursor.execute("select * from professores")
        professores = [
            {"matricula": row[0], "nome": row[1], "email": row[2],
                "telefone": row[3]
            }
            for row in self.cursor.fetchall()
        ]
        self.close()
        return professores

    def getProfessores(self, matricula: int) -> dict:
        self.connect()
        self.cursor.execute(
            f"select * from professores where matricula={matricula}"
        )
        professores = [
            {"matricula": row[0], "nome": row[1], "email": row[2],
                "telefone": row[3]
            }
            for row in self.cursor.fetchall()
        ]
        self.close()
        try:
            return True, professores[0]
        except IndexError:
            return False, "Professor não encontrado"

    def addProfessor(self, matricula, nome, email, telefone):
        self.connect()
        self.cursor.execute('INSERT INTO professores (matricula, nome, email, telefone) VALUES (?,?,?,?)', (matricula nome, email, telefone))
        self.connection.commit()
        self.close()

    def updateNomeProfessor(self, matricula, novo_nome):
        state, professor = self.getAluno(matricula)
        if not professor:
            self.close()
            return False, "Professor não encontrado"

        if professor['nome'] == novo_nome:
            self.close()
            return False, "O novo nome é igual ao atual"

        self.connect()
        self.cursor.execute('UPDATE professores SET nome = ? WHERE matricula = ?', (novo_nome, matricula))
        self.connection.commit()

        state, professor_atualizado = self.getProfessor(matricula)
        if professor_atualizado['nome'] == novo_nome:
            self.close()
            return True, professor_atualizado
        else:
            self.close()
            return False, "Falha ao atualizar o nome"
    
    def calcularCR(self, matricula: str) -> float:
        disciplinas = self.getAllDisciplinas(matricula)

        if not disciplinas:
            return 0.0  # Retorna 0 se o aluno não tiver disciplinas

        total_pontos = 0.0
        total_cargas = 0

        self.connect()

        for disciplina in disciplinas:
            self.cursor.execute(
                """SELECT sim1, sim2, av, avs FROM notas 
                   WHERE aluno=? AND materia=?""",
                (matricula, disciplina['nome'])
            )
            notas = self.cursor.fetchone()

            if notas:
                sim1, sim2, av, avs = notas
                media = (sim1 + sim2 + av + avs) / 4
                total_pontos += media * disciplina['carga']
                total_cargas += disciplina['carga']

        self.close()

        if total_cargas == 0:
            return 0.0

        return total_pontos / total_cargas
