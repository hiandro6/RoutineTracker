from fastapi import FastAPI, Depends, HTTPException
from models import Usuarios, UsuarioCreate
#from models import Usuarios, Atividades, RegistroAtividades, Desafios, ParticipantesDesafios, RegrasDesafios, RegistroDesafio
from sqlmodel import create_engine, SQLModel, Session, select
from typing import Annotated, List
from contextlib import asynccontextmanager
from datetime import datetime, timezone

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

#gerenciamento de sessão
def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)
#usuários:

@app.get("/usuarios")
def get_usuarios():
    pass

@app.post("/usuarios", response_model=Usuarios)
def cadastrar_usuario(usuario: UsuarioCreate, session: SessionDep) -> Usuarios:
    novo_usuario = Usuarios(**usuario.model_dump(), data_criacao=datetime.now(timezone.utc))
    session.add(novo_usuario)
    session.commit()
    session.refresh(novo_usuario)
    return novo_usuario


"""
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
    pass"""
