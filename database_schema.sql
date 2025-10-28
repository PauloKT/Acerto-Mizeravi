-- Script SQL para criar tabela de resultados de quiz
-- Execute este script no seu banco MySQL se estiver usando banco de dados

DROP DATABASE IF EXISTS acerto_mizeravi;

CREATE DATABASE acerto_mizeravi;
USE acerto_mizeravi;

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    login VARCHAR(50) NOT NULL,
    senha VARCHAR(100) NOT NULL,
    data_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    UNIQUE KEY unique_email (email),
    UNIQUE KEY unique_login (login)
);

CREATE TABLE resultados_quiz (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    pontuacao INT NOT NULL,
    total_perguntas INT NOT NULL,
    categoria VARCHAR(50) NOT NULL,
    dificuldade VARCHAR(20) NOT NULL,
    tempo_gasto INT DEFAULT 0,
    data_realizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE,
    INDEX idx_usuario_id (usuario_id),
    INDEX idx_categoria (categoria),
    INDEX idx_dificuldade (dificuldade),
    INDEX idx_data_realizacao (data_realizacao)
);

CREATE INDEX idx_ranking_geral 
ON resultados_quiz (usuario_id, pontuacao DESC);

CREATE INDEX idx_ranking_categoria 
ON resultados_quiz (categoria, usuario_id, pontuacao DESC);