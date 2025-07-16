from sqlmodel import SQLModel, Field
from datetime import datetime, date, timezone
from typing import Optional

class UsuarioCreate(SQLModel):
    nome: str
    email: str
    nivel: int
    pontuacao: int
    
class Usuarios(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str
    email: str
    nivel: int
    pontuacao: int
    data_criacao: datetime = Field(default_factory= lambda: datetime.now(timezone.utc))

# class Atividades(SQLModel):
#     id: int
#     nome: str
#     descricao: str
#     categoria: str
#     pontuacao: int

# class RegistroAtividades(SQLModel):
#     id: int
#     usuario: int
#     atividade: int
#     data_execucao: date
#     pontuacao_recebida: int
#     observacoes: str

# class Desafios(SQLModel):
#     id: int
#     nome: str
#     criador: int
#     descricao: str
#     data_inicio: date
#     data_fim: date
#     status: str

# class ParticipantesDesafios(SQLModel):
#     id: int
#     desafio: int
#     usuario: int
#     pontuacao: int

# class RegrasDesafios(SQLModel):
#     id: int
#     desafio: int
#     atividade: int
#     pontuacao_costumizada: int

# class RegistroDesafio(SQLModel):
#     id: int
#     participante: int
#     atividade: int
#     data_execucao: date
    
