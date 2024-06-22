create database Escola;
use Escola;

create table alunos(
id_aluno int auto_increment primary key not null,
nome varchar(50) not null,
cpf varchar(50) not null);


select * from alunos;