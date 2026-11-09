CREATE DATABASE cineverse;

USE cineverse;

CREATE TABLE catalogo (
    id INT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(100) NOT NULL,
    tipo VARCHAR(20) NOT NULL,
    genero VARCHAR(50) NOT NULL,
    ano INT NOT NULL
);

Registro 1 - 
titulo: Frozen
tipo: Filme
genero: Animacao
ano: 2013

Registro 2 - 
titulo: Vingadores: Ultimato
tipo: Filme
genero: Acao
ano: 2019

Registro 3 - 
titulo: Pousando no Amor
tipo: Serie
genero: Romance
ano: 2019-2020