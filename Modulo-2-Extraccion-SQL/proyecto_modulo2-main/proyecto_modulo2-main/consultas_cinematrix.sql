use cinematrix;

show tables;

select * from caracteristicas_imdb;

select * from informacion_moviedatabase;

select * from oscars;

select * from datos_actores;

ALTER TABLE `datos_actores` MODIFY `fecha_nacimiento` VARCHAR(20);


-- 1. Seleccionamos el año con la puntuación media más alta:
SELECT 
    imd.año,
    ROUND(AVG(puntuacion),2) AS puntuacion_media
FROM 
    caracteristicas_imdb ci
JOIN 
    informacion_moviedatabase imd
ON 
    ci.id_imdb = imd.id
GROUP BY 
    imd.año
ORDER BY 
    puntuacion_media DESC -- en orden descendente para que vaya de mayor a menor
LIMIT 1; -- seleccionamos sólo el primer y mayor resultado


-- 2. ¿En qué años se estrenaron más películas?
SELECT 
    año,
    COUNT(*) AS cantidad_peliculas
FROM 
    informacion_moviedatabase
GROUP BY 
    año
ORDER BY 
    cantidad_peliculas DESC 
LIMIT 5; 

-- 3. ¿En qué año se estrenaron más cortos?
SELECT año, COUNT(*) AS cantidad_cortometrajes
FROM informacion_moviedatabase
WHERE tipo = 'Short'
GROUP BY año
ORDER BY cantidad_cortometrajes DESC
LIMIT 1;

-- 4. ¿Cuál es el metraje mejor valorado en IMDB?
SELECT 
    titulo, tipo,
    puntuacion
FROM 
    caracteristicas_imdb
ORDER BY 
    puntuacion DESC
LIMIT 1;


-- 5. ¿Hay algun actor/actriz que haya recibido más de un premio Óscar?
SELECT nombre_apellido, COUNT(*) AS cantidad_premios_oscar
FROM (
    SELECT actor AS nombre_apellido FROM oscars
    UNION ALL
    SELECT actriz AS nombre_apellido FROM oscars
) AS actores_oscar
GROUP BY nombre_apellido
HAVING cantidad_premios_oscar > 1;
-- La RESPUESTA es no, por lo cual el resultado aparece vacío.


-- 6. ¿Cuántas películas tienen en su argumento la palabra 'amor'?
SELECT 
    COUNT(*) AS cantidad_peliculas_con_amor
FROM 
    caracteristicas_imdb
WHERE 
    argumento LIKE '%amor%';


-- 7. ¿Cuántas películas tienen en su argumento la palabra 'terror'?
SELECT 
    COUNT(*) AS cantidad_peliculas_con_terror
FROM 
    caracteristicas_imdb
WHERE 
    argumento LIKE '%terror%';


-- 9. Actores y actrices con más películas relevantes mencionadas
SELECT 
    nombre_apellido,
    LENGTH(peliculas_relevantes) - LENGTH(REPLACE(peliculas_relevantes, ',', '')) + 1 AS cantidad_peliculas
FROM 
    datos_actores
HAVING
    cantidad_peliculas > 2
ORDER BY 
    cantidad_peliculas DESC;















