from typing import Optional, List
from datetime import date, datetime
from enum import Enum

from sqlmodel import SQLModel, Field, Relationship, UniqueConstraint
from sqlalchemy import func, Enum as SAEnum


# ---------- Enums ----------

class StatusDesafio(str, Enum):
    ESPERANDO_PARTICIPANTES = "Esperando Participantes"
    ATIVO = "Ativo"
    FINALIZADO = "Finalizado"


# ---------- Usuário e Schemas ----------

class UsuarioBase(SQLModel):
    nome: Optional[str] = Field(default=None, max_length=200)
    email: Optional[str] = Field(default=None, max_length=200)
    

class UsuarioCreate(UsuarioBase):
    nome: str
    email: str
    senha: str  # em produção você deve hashear antes de salvar


class UsuarioRead(SQLModel):
    id: int
    nome: str
    email: str
    nivel: int
    pontuacao: int
    data_criacao: datetime


class UsuarioUpdate(SQLModel):
    nome: Optional[str] = None
    email: Optional[str] = None
    senha: Optional[str] = None
    nivel: Optional[int] = None
    pontuacao: Optional[int] = None


class Usuario(SQLModel, table=True):
    __tablename__ = "usuarios"

    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str = Field(nullable=False, max_length=200)
    email: str = Field(nullable=False, unique=True, index=True, max_length=200)
    senha: str = Field(nullable=False, max_length=255)
    nivel: int = Field(default=1)
    pontuacao: int = Field(default=0)
    data_criacao: datetime = Field(default_factory=datetime.utcnow, sa_column_kwargs={"server_default": func.current_timestamp()})

    registro_atividades: List["RegistroAtividade"] = Relationship(back_populates="usuario")
    participantes_desafios: List["ParticipanteDesafio"] = Relationship(back_populates="usuario")


# ---------- Atividade e Schema ----------

class AtividadeBase(SQLModel):
    nome: Optional[str] = Field(default=None, max_length=100)
    descricao: Optional[str] = None
    categoria: Optional[str] = Field(default=None, max_length=50)
    pontuacao: Optional[int] = None


class AtividadeCreate(AtividadeBase):
    nome: str
    pontuacao: int


class Atividade(AtividadeBase, table=True):
    __tablename__ = "atividades"

    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str = Field(nullable=False, max_length=100)
    descricao: Optional[str] = None
    categoria: Optional[str] = None
    pontuacao: int = Field(nullable=False)

    registro_atividades: List["RegistroAtividade"] = Relationship(back_populates="atividade")
    regras_desafio: List["RegraDesafio"] = Relationship(back_populates="atividade")
    registro_desafio: List["RegistroDesafio"] = Relationship(back_populates="atividade")


# ---------- Desafio e Schema ----------

class DesafioBase(SQLModel):
    nome: Optional[str] = Field(default=None, max_length=100)
    descricao: Optional[str] = None
    data_inicio: Optional[date] = None
    data_fim: Optional[date] = None
    status: Optional[StatusDesafio] = None


class DesafioCreate(DesafioBase):
    nome: str
    data_inicio: date
    data_fim: date


class Desafio(DesafioBase, table=True):
    __tablename__ = "desafios"

    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str = Field(nullable=False, max_length=100)
    criador_id: Optional[int] = Field(foreign_key="usuarios.id", default=None)
    descricao: Optional[str] = None
    data_inicio: date = Field(nullable=False)
    data_fim: date = Field(nullable=False)
    status: StatusDesafio = Field(default=StatusDesafio.ESPERANDO_PARTICIPANTES, sa_column=SAEnum(StatusDesafio))

    participantes: List["ParticipanteDesafio"] = Relationship(back_populates="desafio")
    regras: List["RegraDesafio"] = Relationship(back_populates="desafio")


# ---------- Outras entidades (referenciadas pelas relações, podem ficar em arquivos separados se quiser) ----------

class ParticipanteDesafio(SQLModel, table=True):
    __tablename__ = "participantes_desafios"

    id: Optional[int] = Field(default=None, primary_key=True)
    desafio_id: int = Field(foreign_key="desafios.id", nullable=False)
    usuario_id: int = Field(foreign_key="usuarios.id", nullable=False)
    pontuacao: int = Field(default=0)

    desafio: Optional[Desafio] = Relationship(back_populates="participantes")
    usuario: Optional[Usuario] = Relationship(back_populates="participantes_desafios")
    registros_desafio: List["RegistroDesafio"] = Relationship(back_populates="participante")


ParticipanteDesafio.__table_args__ = (UniqueConstraint("desafio_id", "usuario_id", name="uq_desafio_usuario"),)


class RegraDesafio(SQLModel, table=True):
    __tablename__ = "regras_desafio"

    id: Optional[int] = Field(default=None, primary_key=True)
    desafio_id: int = Field(foreign_key="desafios.id", nullable=False)
    atividade_id: int = Field(foreign_key="atividades.id", nullable=False)
    pontuacao_costumizada: int = Field(nullable=False)

    desafio: Optional[Desafio] = Relationship(back_populates="regras")
    atividade: Optional[Atividade] = Relationship(back_populates="regras_desafio")


class RegistroAtividade(SQLModel, table=True):
    __tablename__ = "registro_atividades"

    id: Optional[int] = Field(default=None, primary_key=True)
    usuario_id: int = Field(foreign_key="usuarios.id", nullable=False)
    atividade_id: int = Field(foreign_key="atividades.id", nullable=False)
    data_execucao: date = Field(nullable=False)
    pontuacao_recebida: int = Field(nullable=False)
    observacoes: Optional[str] = None

    usuario: Optional[Usuario] = Relationship(back_populates="registro_atividades")
    atividade: Optional[Atividade] = Relationship(back_populates="registro_atividades")


class RegistroDesafio(SQLModel, table=True):
    __tablename__ = "registro_desafio"

    id: Optional[int] = Field(default=None, primary_key=True)
    participante_id: int = Field(foreign_key="participantes_desafios.id", nullable=False)
    atividade_id: int = Field(foreign_key="atividades.id", nullable=False)
    data_execucao: date = Field(nullable=False)

    participante: Optional[ParticipanteDesafio] = Relationship(back_populates="registros_desafio")
    atividade: Optional[Atividade] = Relationship(back_populates="registro_desafio")
    