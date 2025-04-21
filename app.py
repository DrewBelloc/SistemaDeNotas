from flask import Flask, render_template
import sqlite3

app = Flask(__name__)  # TEM QUE vir antes de qualquer @app.route

@app.route("/teste")
def test():
    connection = sqlite3.connect("banco.db")
    cursor = connection.cursor()

    # Busca só os alunos
    cursor.execute("SELECT nome FROM alunos")
    alunos = [{"nome": row[0], "tipo": "Aluno"} for row in cursor.fetchall()]

    connection.close()

    # Ordena os alunos por nome
    alunos.sort(key=lambda x: x["nome"])

    return render_template("teste.html", itens=alunos)
