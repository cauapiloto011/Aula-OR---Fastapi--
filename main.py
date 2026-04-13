from fastapi import FastAPI

#Inicializar o fastapi
app = FastAPI(title="Gestão escolar")

#Rodar api
# no terminal: python -m uvicorn main:app --reload

#Rota
# Métodos http: GET, POST, PUT, DELETE
@app.get("/")
def tela_inicial():
    return { "mensagem": "Bem-vindo ao sistema de gestão escolar" }

#Banco de dados
alunos = {
    1: {"nome": "Caua", "idade": 34},
    2: {"nome": "Melyssa", "idade": 18},
    3: {"nome": "Leo", "idade": 48},
}

@app.get("/alunos")
def listar_alunos():
    return { "alunos": alunos}
