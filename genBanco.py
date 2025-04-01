import random
import sqlite3

connection = sqlite3.connect("banco.db")
cursor = connection.cursor()
cursor.execute("create table alunos (matricula text, nome text, ano integer)")
cursor.execute("create table materias (codigo integer, nome text, carga integer)")
cursor.execute("create table notas (materia text, aluno text, periodo integer, sim1 float, sim2 float, av float, avs float)")

nomes = [
    "Helena",
    "Alice",
    "Laura",
    "Maria Alice",
    "Sophia",
    "Manuela",
    "Maitê",
    "Liz",
    "Cecília",
    "Isabella",
    "Luísa",
    "Heloísa",
    "Eloá",
    "Júlia",
    "Ayla",
    "Maria Luísa",
    "Isis",
    "Elisa",
    "Antonella",
    "Valentina",
    "Maya",
    "Maria Júlia",
    "Aurora",
    "Lara",
    "Maria Clara",
    "Lívia",
    "Esther",
    "Giovanna",
    "Sarah",
    "Maria Cecília",
    "Lorena",
    "Beatriz",
    "Luna",
    "Olivia",
    "Maria Helena",
    "Mariana",
    "Isadora",
    "Melissa",
    "Maria",
    "Catarina",
    "Lavinia",
    "Alicia",
    "Maria Eduarda",
    "Agatha",
    "Ana Liz",
    "Yasmin",
    "Emanuelly",
    "Ana Clara",
    "Clara",
    "Miguel",
    "Arthur",
    "Gael",
    "Théo",
    "Heitor",
    "Ravi",
    "Davi",
    "Bernado",
    "Noah",
    "Gabriel",
    "Samuel",
    "Pedro",
    "Anthony",
    "Isaac",
    "Benício",
    "Benjamin",
    "Matheus",
    "Lucas",
    "Joaquim",
    "Nicolas",
    "Lucca",
    "Lorenzo",
    "Henrique",
    "João Miguel",
    "Rafael",
    "Henry",
    "Murilo",
    "Levi",
    "Guilherme",
    "Vicente",
    "Felipe",
    "Bryan",
    "Matteo",
    "Bento",
    "João Pedro",
    "Pietro",
    "Leonardo",
    "Daniel",
    "Gustavo",
    "Pedro Henrique",
    "João Lucas",
    "Emanuel",
    "João",
    "Caleb",
    "Davi Lucca",
    "Antônio",
    "Eduardo",
    "Enrico",
    "Caio",
    "José"
]

sobrenomes = [
    "Da Silva",
    "Pereira",
    "Ferreira",
    "Silva",
    "De Souza",
    "Santos",
    "Ribeiro",
    "Martins",
    "Barbosa",
    "Vieira",
    "Fernandes",
    "Costa",
    "De Souza",
    "De Lima",
    "Moreira",
    "Da Costa",
    "Mendes",
    "Araujo",
    "Teixeira",
    "Almeida",
    "Machado",
    "Nascimento",
    "Bezerra",
    "Dos Santos",
    "Alves",
    "De Oliveira",
    "De Jesus",
    "Soares",
    "Lopes",
    "Souza",
    "Lima",
    "Batista",
    "Dias",
    "Do Nascimento",
    "Nunes",
    "De Almeida",
    "Carvalho",
    "Cardoso",
    "Marques",
    "Ramos",
    "Rocha",
    "De Araujo",
    "Sousa"
    "Borges",
    "Aparecido",
    "Pinheiro",
    "Andrade",
    "Leite",
    "Nogueira",
    "Da Cruz",
    "Tavares",
    "De Freitas",
    "Pires",
    "Miranda",
    "Freitas",
    "Dos Reis",
    "Do Carmo",
    "Moraes",
    "De Melo",
    "Viana",
    "Moura"
]

anos = [2019,2020,2021,2022,2023,2024]
anos = random.choices(anos, k=50)

alunos = [(
    str(ano)+str(random.randint(1000,9999)),
    f"{random.choice(nomes)} {random.choice(sobrenomes)}",
    ano
    ) for ano in anos
]

cursor.executemany("insert into alunos values (?,?,?)", alunos)

materias = [
    ["INTRODUÇÃO A PROGRAMAÇÃO DE COMPUTADORES",80],
    ["ARQUITETURA DE COMPUTADORES",80],
    ["FUNDAMENTOS DE REDES DE COMPUTADORES",80],
    ["INTRODUÇÃO À SEGURANÇA DA INFORMAÇÃO",80],
    ["PENSAMENTO COMPUTACIONAL",80],
    ["BANCO DE DADOS",80],
    ["DESENV. WEB EM HTML5, CSS, JAVASCRIPT E PHP",80],
    ["PARADIGMAS DE LINGUAGENS DE PROGRAMAÇÃO EM PYTHON",80],
    ["COMPUTAÇÃO EM NUVEM",80],
    ["DESENVOLVIMENTO RÁPIDO DE APLICAÇÕES EM PYTHON",80],
    ["ESTRUTURA DE DADOS",80],
    ["MATEMÁTICA E LÓGICA",80],
    ["PROTOCOLOS DE REDES DE COMPUTADORES",80],
    ["SISTEMAS OPERACIONAIS",80],
    ["SISTEMAS DE INFORMAÇÃO E SOCIEDADE",80],
    ["ANÁLISE DE DADOS",80],
    ["CÁLCULO DIFERENCIAL E INTEGRAL",80],
    ["PROGRAMAÇÃO DE SOFTWARE BÁSICO EM C",80],
    ["SISTEMAS DIGITAIS",80],
    ["MODELAGEM DE SISTEMAS EM UML",80],
    ["CÁLCULO DE MÚLTIPLAS VARIÁVEIS",80],
    ["GEOMETRIA ANALÍTICA E ÁLGEBRA LINEAR",80],
    ["SISTEMAS DISTRIBUÍDOS E COMPUTAÇÃO PARALELA",80],
    ["ALGORITMOS E COMPLEXIDADE",80],
    ["ENGENHARIA DE SOFTWARE",80],
    ["PROGRAMAÇÃO ORIENTADA A OBJETOS EM JAVA",80],
    ["MÉTODOS QUANTITATIVOS",80],
    ["ALGORITMOS EM GRAFOS",80],
    ["PROGRAMAÇÃO DE MICROCONTROLADORES",80],
    ["LINGUAGENS FORMAIS E AUTÔMATOS",80],
    ["APLIC. DE CLOUD, IOT E INDÚSTRIA 4.0 EM PYTHON",80],
    ["INTELIGÊNCIA ARTIFICIAL",80],
    ["PROGRAMAÇÃO PARA DISPOSITIVOS MÓVEIS EM ANDROID",80],
    ["PADRÕES DE PROJETOS DE SOFTWARE COM JAVA",80],
    ["MODELAGEM MATEMÁTICA",80],
    ["TÓPICOS EM LIBRAS: SURDEZ E INCLUSÃO",80],
    ["TÓPICOS DE BIG DATA EM PYTHON",80],
    ["ALGORITMOS DE PROCESSAMENTO DE IMAGEM",80],
    ["COMPILADORES",80],
    ["SEGURANÇA CIBERNÉTICA",80]
]

materiasSQL = [(
    i,materias[i][0],materias[i][1]
    ) for i in range(len(materias))
]

cursor.executemany("insert into materias values (?,?,?)", materiasSQL)

notas = []
materiasAlunos = {}

for aluno in alunos:
    periodo = 2025 - aluno[2]
    materiasAlunos[aluno[1]] = []
    for i in range(periodo):
        for i in range(5):
            check = True
            materia = ""
            while check:
                materia = random.choice(materias)
                materia = materia[0]
                if materia in materiasAlunos[aluno[1]]:
                    pass
                else:
                    materiasAlunos[aluno[1]].append(materia)
                    check = False
            sim1 = float(random.randint(0,1)/2)
            sim2 = float(random.randint(0,1)/2)
            av = float(random.randint(0,10))
            avs = float(random.randint(0,10))
            notas.append((materia,aluno[0],2025-aluno[2],sim1,sim2,av,avs))

cursor.executemany("insert into notas values (?,?,?,?,?,?,?)", notas)

connection.close()
