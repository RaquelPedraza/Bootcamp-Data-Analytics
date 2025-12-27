-- Crear la base de datos
CREATE SCHEMA CINEMATRIX; 

-- Usar la base de datos
USE CINEMATRIX;


ALTER TABLE `caracteristicas_imdb` DROP FOREIGN KEY `caracteristicas_imdb_ibfk_1`;

-- Eliminar la tabla existente si es necesario
DROP TABLE IF EXISTS `informacion_moviedatabase`;

-- Crear la tabla ajustada (API)
CREATE TABLE `informacion_moviedatabase` (
    tipo VARCHAR(25), 
    titulo VARCHAR(100), 
    año INT, 
    mes INT,
    id VARCHAR(25),
    PRIMARY KEY (id)
);

SELECT * 
FROM informacion_moviedatabase;


ALTER TABLE `caracteristicas_imdb`
ADD CONSTRAINT `caracteristicas_imdb_ibfk_1` FOREIGN KEY (`id_imdb`) REFERENCES `informacion_moviedatabase` (`id`);

-- Crear la tabla IMDB
CREATE TABLE `caracteristicas_imdb` (
    id_imdb VARCHAR(25), 
    titulo VARCHAR(100), 
    tipo VARCHAR(25), 
    director VARCHAR(250), 
    guionista1 VARCHAR(250), 
    guionista2 VARCHAR(250), 
    duracion VARCHAR(25), 
    puntuacion FLOAT, 
    argumento VARCHAR(370),
    PRIMARY KEY (titulo),
    FOREIGN KEY (id_imdb) REFERENCES `informacion_moviedatabase`(id)
);

ALTER TABLE caracteristicas_imdb MODIFY argumento TEXT;

SELECT *
from caracteristicas_imdb;

-- Crear la tabla características actores
CREATE TABLE `datos_actores` (
    nombre_apellido VARCHAR(50), 
    fecha_nacimiento VARCHAR(5), 
    premios_oscar VARCHAR(50),
    peliculas_relevantes VARCHAR(500), 
    profesiones VARCHAR(100),
    PRIMARY KEY (nombre_apellido)
);
ALTER TABLE `datos_actores` MODIFY `fecha_nacimiento` VARCHAR(20);
select * from datos_actores;

-- Crear la tabla oscars
CREATE TABLE `oscars` (
    ceremonia VARCHAR(5), 
    mejor_pelicula VARCHAR(100), 
    mejor_director VARCHAR(100),
    mejor_actor VARCHAR(100), 
    mejor_actriz VARCHAR(100), 
    mejor_actor_reparto VARCHAR(100), 
    mejor_actriz_reparto VARCHAR(100),
    FOREIGN KEY (mejor_actor) REFERENCES `datos_actores`(nombre_apellido),
    FOREIGN KEY (mejor_actriz) REFERENCES `datos_actores`(nombre_apellido),
    FOREIGN KEY (mejor_actor_reparto) REFERENCES `datos_actores`(nombre_apellido),
    FOREIGN KEY (mejor_actriz_reparto) REFERENCES `datos_actores`(nombre_apellido)
);

-- Transferir datos de 'oscars' a 'oscar'
INSERT INTO oscar (ano_ceremonia, pelicula, director, actor, actriz)
SELECT 
    CONVERT(ceremonia, UNSIGNED),
    mejor_pelicula,
    mejor_director,
    mejor_actor,
    mejor_actriz
FROM oscars;

-- Verificar que los datos se han transferido correctamente
SELECT * FROM oscars;


-- Verificar que la tabla ha sido renombrada correctamente
SHOW TABLES;




