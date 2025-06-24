from pydantic import BaseModel
from datetime import datetime, date

class Usuarios(BaseModel):
    id: int
    nome: str
    email: str
    nivel: int
    pontuacao: int
    data_criacao: datetime

class Atividades(BaseModel):
    id: int
    nome: str
    descricao: str
    categoria: str
    pontuacao: int

class RegistroAtividades(BaseModel):
    id: int
    usuario: int
    atividade: int
    data_execucao: date
    pontuacao_recebida: int
    observacoes: str

class Desafios(BaseModel):
    id: int
    nome: str
    criador: int
    descricao: str
    data_inicio: date
    data_fim: date
    status: str

class ParticipantesDesafios(BaseModel):
    id: int
    desafio: int
    usuario: int
    pontuacao: int

class RegrasDesafios(BaseModel):
    id: int
    desafio: int
    atividade: int
    pontuacao_costumizada: int

class RegistroDesafio(BaseModel):
    id: int
    participante: int
    atividade: int
    data_execucao: date
    
