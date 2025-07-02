from fastapi import FastAPI, HTTPException
from models import Usuarios, Atividades, RegistroAtividades, Desafios, ParticipantesDesafios, RegrasDesafios, RegistroDesafio

app = FastAPI()

#usuários:
@app.get("/usuarios", response_model=Usuarios)
def get_usuarios():
    pass

@app.post("/usuarios", response_model=Usuarios)
def cadastrar_usuario():
    pass

@app.put("/usuarios", response_model=Usuarios)
def editar_usuario():
    pass

@app.delete("/usuarios", response_model=Usuarios)
def deletar_usuario():
    pass


#atividades:
@app.get("/atividades", response_model=Atividades)
def get_atividades():
    pass

@app.post("/atividades", response_model=Atividades)
def cadastrar_atividade():
    pass

@app.put("/atividades", response_model=Atividades)
def editar_atividade():
    pass

@app.delete("/atividades", response_model=Atividades)
def deletar_atividade():
    pass



#desafios:
@app.get("/desafios", response_model=Desafios)
def get_desafios():
    pass

@app.post("/desafios", response_model=Desafios)
def cadastrar_desafio():
    pass

@app.put("/desafios", response_model=Desafios)
def editar_desafio():
    pass

@app.delete("/desafios", response_model=Desafios)
def deletar_desafio():
    pass
