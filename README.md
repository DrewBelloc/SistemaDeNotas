# SistemaDeNotas
Um sistema simples para calcular media de notas de alunos

## Setup

Antes de tudo confirme que python e pip estão instalados na sua maquina

> No Windows
`python --version`
`pip --version`

> No Linux/Mac
`python3 --version`
`pip3 --version`

Instale as dependencias na sua maquina usando

> Windows
`pip install -r requirements.txt`

> Linux/Mac
`pip3 install -r requirements.txt`

## Inicializar

Antes de inicializar pela primeira vez é importante gerar um banco de dados inicial.

> Windows
`python .\genBanco.py`

> Linux/Mac
`python3 genBanco.py`

Com o arquivo `banco.db` no root do projeto você pode inicializar o servidor usando

`flask run --debug`
