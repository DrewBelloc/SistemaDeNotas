import sqlite3
from flask import Flask, request, render_template

app = Flask(__name__)

# Rota para a tela padrão
@app.route("/") # Define a URL que o cliente irá acessar
def index(): # Função que será ativada quando o cliente acessar a URL acima
    return render_template("script.html") # Faz a construção da pagina e retorna para  cliente no navegador

if __name__=="__main__": # Faz uma checagem para confirmar que esse é o modulo principal
    main() # Inicia o servidor
