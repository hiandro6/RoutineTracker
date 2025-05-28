CREATE DATABASE db_routine_tracker;
USE db_routine_tracker;

CREATE TABLE usuarios(
	id int auto_increment primary key,
	nome varchar(200) not null,
	email varchar(200) not null unique,
	senha varchar(255) not null,
	nivel int default 1,
	pontuacao int default 0,
	data_criacao timestamp default current_timestamp
);

CREATE TABLE atividades(
	id int auto_increment primary key,
	nome varchar(100) not null,
    descricao text,
    categoria varchar(50),
    pontuacao int not null
);

CREATE TABLE registro_atividades(
	id int auto_increment primary key,
    usuario int,
    atividade int,
    data_execucao date not null,
    pontuacao_recebida int not null,
    observacoes text,
    foreign key (usuario) references usuarios(id) on delete cascade,
    foreign key (atividade) references atividades(id) on delete cascade
);

CREATE TABLE desafios(
	id int auto_increment primary key,
    nome varchar(100) not null,
    criador int,
    descricao text,
    data_inicio date not null,
    data_fim date not null,
    status enum('Esperando Participantes', 'Ativo', 'Finalizado') default 'Esperando Participantes'
);

CREATE TABLE participantes_desafios(
	id int auto_increment primary key,
    desafio int,
    usuario int,
    pontuacao int default 0,
    foreign key (desafio) references desafios(id) on delete cascade,
    foreign key (usuario) references usuarios(id) on delete cascade,
    unique (desafio, usuario)
);

CREATE TABLE regras_desafio(
	id int auto_increment primary key,
    desafio int,
    atividade int,
    pontuacao_costumizada int not null,
    foreign key (desafio) references desafios(id) on delete cascade,
    foreign key (atividade) references atividades(id) on delete cascade
);

CREATE TABLE registro_desafio(
	id int auto_increment primary key,
    participante int,
    atividade int,
    data_execucao date not null,
    foreign key (participante) references participantes_desafios(id),
    foreign key (atividade) references atividades(id)
);

