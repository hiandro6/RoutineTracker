from fastapi import FastAPI, Depends, HTTPException, Path, Query, status
from sqlmodel import Session, select, SQLModel, create_engine
from typing import Annotated, List
from contextlib import asynccontextmanager
from datetime import datetime, timezone
from sqlalchemy import event
from fastapi.middleware.cors import CORSMiddleware

# seus modelos
from models import (
    Usuario,
    UsuarioCreate,
    UsuarioRead,
    UsuarioUpdate,
    Atividade,
    AtividadeCreate,
    Desafio,
    DesafioCreate,
)

# SQLite config
sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
engine = create_engine(
    sqlite_url, echo=True, connect_args={"check_same_thread": False}
)

# Habilita foreign_keys para cada conexão SQLite
@event.listens_for(engine, "connect")
def _set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON;")
    cursor.close()


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


# Dependência de sessão
def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ou restrinja para seu frontend
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---------- Usuários ----------

@app.get("/usuarios", response_model=List[UsuarioRead])
def listar_usuarios(
    *,
    session: SessionDep,
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
):
    statement = select(Usuario).offset(skip).limit(limit)
    usuarios = session.exec(statement).all()
    return usuarios


@app.post(
    "/usuarios",
    response_model=UsuarioRead,
    status_code=status.HTTP_201_CREATED,
    summary="Cadastrar novo usuário",
)
def cadastrar_usuario(*, usuario: UsuarioCreate, session: SessionDep) -> Usuario:
    existing = session.exec(select(Usuario).where(Usuario.email == usuario.email)).first()
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Email já cadastrado"
        )
    novo_usuario = Usuario(**usuario.model_dump(), data_criacao=datetime.now(timezone.utc))
    session.add(novo_usuario)
    session.commit()
    session.refresh(novo_usuario)
    return novo_usuario


@app.put("/usuarios/{usuario_id}", response_model=UsuarioRead)
def editar_usuario(
    *,
    usuario_id: int = Path(..., ge=1),
    usuario_update: UsuarioUpdate,
    session: SessionDep
):
    usuario = session.get(Usuario, usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    if usuario_update.email and usuario_update.email != usuario.email:
        existing = session.exec(select(Usuario).where(Usuario.email == usuario_update.email)).first()
        if existing:
            raise HTTPException(status_code=400, detail="Email já em uso por outro usuário")

    usuario_data = usuario_update.model_dump(exclude_unset=True)
    for key, value in usuario_data.items():
        setattr(usuario, key, value)

    session.add(usuario)
    session.commit()
    session.refresh(usuario)
    return usuario


@app.delete("/usuarios/{usuario_id}", response_model=UsuarioRead)
def deletar_usuario(*, usuario_id: int = Path(..., ge=1), session: SessionDep):
    usuario = session.get(Usuario, usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    session.delete(usuario)
    session.commit()
    return usuario


# ---------- Esboço para Atividades e Desafios ----------

@app.get("/atividades", response_model=List[Atividade])
def listar_atividades(*, session: SessionDep, skip: int = 0, limit: int = 100):
    statement = select(Atividade).offset(skip).limit(limit)
    return session.exec(statement).all()


@app.post("/atividades", response_model=Atividade, status_code=status.HTTP_201_CREATED)
def cadastrar_atividade(*, atividade: AtividadeCreate, session: SessionDep):
    novo = Atividade(**atividade.model_dump())
    session.add(novo)
    session.commit()
    session.refresh(novo)
    return novo


@app.get("/desafios", response_model=List[Desafio])
def listar_desafios(*, session: SessionDep, skip: int = 0, limit: int = 100):
    statement = select(Desafio).offset(skip).limit(limit)
    return session.exec(statement).all()


@app.post("/desafios", response_model=Desafio, status_code=status.HTTP_201_CREATED)
def cadastrar_desafio(*, desafio: DesafioCreate, session: SessionDep):
    novo = Desafio(**desafio.model_dump())
    session.add(novo)
    session.commit()
    session.refresh(novo)
    return novo
