from banco import Banco
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)
db = Banco()


# Rota para a tela padrão
@app.route("/")  # Define a URL que o cliente irá acessar
def index():  # Função que será ativada quando o cliente acessar a URL acima
    alunos = db.getAllAlunos()
    # Ordena os alunos por nome
    alunos.sort(key=lambda x: x["nome"])
    return render_template("lista.html", itens=alunos)


@app.route("/aluno/<matricula>")
def aluno(matricula):
    status, aluno = db.getAluno(matricula)
    if status:
        return f"<h1>{aluno['nome']}</h1>"
    else:
        return aluno


@app.route("/alunos/")
def alunos():
    alunos = db.getAllAlunos()
    html = ""
    for i in alunos:
        html += f"<h2>{i['nome']}</h2>\n"
    return html


@app.route("/editar/<matricula>")
def editar(matricula):
    aluno = db.getAluno(matricula)
    return f"<h1>{aluno['nome']}</h1>"


@app.route("/teste/<disciplina>")
def testeback(disciplina):
    status, aluno = db.getAlunos(disciplina)
    if status:
        return f"{aluno}"
    else:
        return aluno

@app.route("/add")
def addAluno():
    db.addAluno("20256969","Mandy")
    return redirect("/")

@app.route("/teste")
def test():
    return render_template("telacadastro.html")



# checagem confirmando que esse é o modulo principal
if __name__ == "__main__":
    app.run()  # Inicia o servidor flask.
