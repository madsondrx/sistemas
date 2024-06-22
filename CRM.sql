create database crm_db;
use crm_db;

create table registros(
id_registros int auto_increment primary key not null,
nome varchar(50) not null,
cpf varchar(50) not null,
email varchar(50) not null,
ultima_compra varchar (50) not null);

select * from registros;