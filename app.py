from banco import Banco
from flask import Flask, render_template

app = Flask(__name__)
db = Banco()

# Rota para a tela padrão


@app.route("/")  # Define a URL que o cliente irá acessar
def index():  # Função que será ativada quando o cliente acessar a URL acima
    return render_template("script.html")


@app.route("/teste")
def test():
    db.connect()

    # Busca só os alunos
    db.cursor.execute("SELECT nome FROM alunos")
    alunos = [
        {"nome": row[0], "tipo": "Aluno"}
        for row in db.cursor.fetchall()
    ]
    db.close()

    # Ordena os alunos por nome
    alunos.sort(key=lambda x: x["nome"])

    return render_template("teste.html", itens=alunos)


# checagem confirmando que esse é o modulo principal
if __name__ == "__main__":
    app.run()  # Inicia o servidor flask.
