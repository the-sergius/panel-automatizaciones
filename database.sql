CREATE DATABASE IF NOT EXISTS panel_automatizaciones;

USE panel_automatizaciones;

CREATE TABLE IF NOT EXISTS usuarios (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre_usuario VARCHAR(50) NOT NULL,
    email_usuario VARCHAR(50) NOT NULL UNIQUE,
    password_usuario VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS servicios (
    id_servicio INT AUTO_INCREMENT PRIMARY KEY,
    nombre_servicio VARCHAR(50) NOT NULL,
    descripcion_servicio VARCHAR(200) NOT NULL
);