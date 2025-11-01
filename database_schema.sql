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

CREATE TABLE ranking_usuarios (
    usuario_id INT PRIMARY KEY,
    maior_pontuacao INT DEFAULT 0,
    media_pontuacao DECIMAL(5,2) DEFAULT 0,
    total_quizzes INT DEFAULT 0,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE
);


DELIMITER //

-- Trigger de criar data/hora dos usuarios ao se registrarem
CREATE TRIGGER before_insert_usuario
BEFORE INSERT ON usuarios
FOR EACH ROW
BEGIN
  
    IF NEW.data_registro IS NULL THEN
        SET NEW.data_registro = NOW();
    END IF;
END //

DELIMITER ;

-- Trigger para atualizar o rankin após o resultado do quiz, por usuario. 
DELIMITER //

CREATE TRIGGER after_insert_resultado
AFTER INSERT ON resultados_quiz
FOR EACH ROW
BEGIN
    DECLARE v_maior_pontuacao INT DEFAULT 0;
    DECLARE v_media_pontuacao DECIMAL(5,2) DEFAULT 0;
    DECLARE v_total INT DEFAULT 0;

 
    SELECT 
        IFNULL(MAX(pontuacao), 0),
        IFNULL(AVG(pontuacao), 0),
        COUNT(*)
    INTO v_maior_pontuacao, v_media_pontuacao, v_total
    FROM resultados_quiz
    WHERE usuario_id = NEW.usuario_id;

   
    INSERT INTO ranking_usuarios (usuario_id, maior_pontuacao, media_pontuacao, total_quizzes)
    VALUES (NEW.usuario_id, v_maior_pontuacao, v_media_pontuacao, v_total)
    ON DUPLICATE KEY UPDATE
        maior_pontuacao = v_maior_pontuacao,
        media_pontuacao = v_media_pontuacao,
        total_quizzes = v_total;
END //

DELIMITER ;