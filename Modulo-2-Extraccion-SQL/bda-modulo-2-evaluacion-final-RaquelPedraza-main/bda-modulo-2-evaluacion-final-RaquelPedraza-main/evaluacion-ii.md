USE sakila;


 /*__________Ejercicio 1__________
 Todos los nombres de las películas sin duplicados.*/ 

SELECT DISTINCT title
FROM film;


/*__________Ejercicio 2__________
Nombres de todas las películas con clasificación "PG-13".*/ 
 
SELECT title
FROM film
WHERE rating = 'PG-13';


/*__________Ejercicio 3__________
Título y descripción de todas las películas que contengan la palabra "amazing" en ella.*/ 

SELECT title, description
FROM film
WHERE description LIKE '%amazing%';


/*__________Ejercicio 4__________
Título de todas las películas con una duración mayor a 120 minutos.*/ 

SELECT title
FROM film
WHERE length > 120;


/*__________Ejercicio 5__________
Nombres de todos los actores.*/ 

SELECT first_name, last_name
FROM actor;


/*__________Ejercicio 6__________
Nombre y apellido de los actores con el apellido "Gibson".*/ 

SELECT first_name, last_name
FROM actor
WHERE last_name = 'Gibson';


/*__________Ejercicio 7__________
Nombres de los actores con un actor_id entre 10 y 20.*/ 
 
SELECT first_name, last_name
FROM actor
WHERE actor_id BETWEEN 10 AND 20;


/*__________Ejercicio 8__________
Título de las películas (tabla film) que no tengan clasificación "R" ni "PG-13".*/ 

SELECT title
FROM film
WHERE rating NOT IN ('R', 'PG-13');

  
/*__________Ejercicio 9__________
Cantidad total de películas en cada clasificación de la tabla film. Muestra la clasificación junto con el recuento.*/ 

SELECT rating, COUNT(*) AS total_films
FROM film
GROUP BY rating
ORDER BY total_films DESC;

   
/*__________Ejercicio 10__________
Cantidad total de películas alquiladas por cada cliente. Muestra el ID del cliente, su nombre y apellido junto con la cantidad de películas alquiladas.*/ 

SELECT c.customer_id, c.first_name, c.last_name, COUNT(r.rental_id) AS total_rented_films
FROM customer c
LEFT JOIN rental r ON c.customer_id = r.customer_id
GROUP BY c.customer_id, c.first_name, c.last_name;

-- subquery
SELECT c.customer_id, c.first_name, c.last_name,
       (SELECT COUNT(*)
        FROM rental r
        WHERE r.customer_id = c.customer_id) AS total_rented_films
FROM customer c;

    
/*__________Ejercicio 11__________ 
Cantidad total de películas alquiladas por categoría. Muestra la categoría junto con el recuento de alquileres.*/

-- subquery
SELECT c.name AS category_name, 
       (SELECT COUNT(*)
        FROM film_category fc
        JOIN inventory i ON fc.film_id = i.film_id
        JOIN rental r ON i.inventory_id = r.inventory_id
        WHERE fc.category_id = c.category_id) AS total_rentals
FROM category c;

-- joins
SELECT c.name AS category_name, COUNT(r.inventory_id) AS rental_count
FROM rental r
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film_category fc ON i.film_id = fc.film_id
JOIN category c ON fc.category_id = c.category_id
GROUP BY c.name
ORDER BY category_name;

     
/*__________Ejercicio 12__________
Promedio de duración de las películas para cada clasificación de la tabla
film. Muestra ambos.*/ 

SELECT rating, ROUND(AVG(length),2) 
FROM film
GROUP BY rating;

      
/*__________Ejercicio 13__________
Nombre y apellido de los actores que aparecen en la película con title "Indian Love".*/

SELECT a.first_name, a.last_name
FROM actor a
JOIN film_actor fa ON a.actor_id = fa.actor_id
JOIN film f ON fa.film_id = f.film_id
WHERE f.title = 'Indian Love';
 
       
/*__________Ejercicio 14__________
Título de todas las películas que contengan la palabra "dog" o "cat" en sudescripción.*/ 

SELECT title
FROM film
WHERE description LIKE '%dog%' OR description LIKE '%cat%';

        
/*__________Ejercicio 15__________
Hay algún actor o actriz que no apareca en ninguna película en la tabla film_actor.*/ 

SELECT actor_id, first_name, last_name
FROM actor
WHERE actor_id NOT IN (
    SELECT DISTINCT actor_id
    FROM film_actor
);

         
/*__________Ejercicio 16__________
Título de todas las películas lanzadas entre los años 2005 y 2010.*/ 

SELECT title
FROM film
WHERE release_year BETWEEN 2005 AND 2010;

          
/*__________Ejercicio 17__________
Título de todas las películas que son de la misma categoría que "Family".*/ 

SELECT f.title
FROM film f
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c ON fc.category_id = c.category_id
WHERE c.name = 'Family';

-- subquery
SELECT title
FROM film
WHERE film_id IN (
    SELECT fc.film_id
    FROM film_category fc
    JOIN category c ON fc.category_id = c.category_id
    WHERE c.name = 'Family'
);

           
/*__________Ejercicio 18__________
Nombre y apellido de los actores que aparecen en más de 10 películas.*/ 

SELECT a.first_name, a.last_name
FROM actor a
JOIN film_actor fa ON a.actor_id = fa.actor_id
GROUP BY a.actor_id
HAVING COUNT(*) > 10;

            
/*__________Ejercicio 19__________
Título de todas las películas que son "R" y tienen una duración mayor a 2 horas en la tabla film.*/

SELECT title
FROM film
WHERE rating = 'R'
AND length > 120;

             
/*__________Ejercicio 20__________
Categorías de películas que tienen un promedio de duración superior a 120 minutos. Muestra la categoría junto con el promedio.*/

WITH category_average_duration AS (
    SELECT c.name AS category_name, ROUND(AVG(f.length),2) AS average_duration
    FROM film f
    JOIN film_category fc ON f.film_id = fc.film_id
    JOIN category c ON fc.category_id = c.category_id
    GROUP BY c.name  -- Agrupa los resultados por nombre de categoría.
)
SELECT category_name, average_duration
FROM category_average_duration
WHERE average_duration > 120;

	
/*__________Ejercicio 21__________ 
Actores que han actuado en al menos 5 películas. Muestra el nombre del actor junto con la cantidad de películas en las que ha actuado.*/

SELECT a.first_name, a.last_name, COUNT(fa.film_id) AS film_count
FROM actor a
JOIN film_actor fa ON a.actor_id = fa.actor_id
GROUP BY a.actor_id
HAVING COUNT(fa.film_id) >= 5;

-- subquery
SELECT first_name, last_name, film_count
FROM (
    SELECT a.first_name, a.last_name, COUNT(fa.film_id) AS film_count
    FROM actor a
    JOIN film_actor fa ON a.actor_id = fa.actor_id
    GROUP BY a.actor_id
) AS actor_film_count
WHERE film_count >= 5;

-- CTE
WITH ActorFilmCount AS (
    SELECT a.first_name, a.last_name, COUNT(fa.film_id) AS film_count
    FROM actor a
    JOIN film_actor fa ON a.actor_id = fa.actor_id
    GROUP BY a.actor_id
)
SELECT first_name, last_name, film_count
FROM ActorFilmCount
WHERE film_count >= 5;


/*__________Ejercicio 22__________
Título de todas las películas que fueron alquiladas más de 5 días. Utiliza una subconsulta para encontrar los rental_ids 
con una duración superior a 5 días y luego selecciona las películas correspondientes.*/ 

SELECT f.title
FROM film f
JOIN inventory i ON f.film_id = i.film_id
WHERE i.inventory_id IN (
    SELECT r.inventory_id
    FROM rental r
    WHERE DATEDIFF(r.return_date, r.rental_date) > 5 -- La función devuelve la diferencia en días (date1, date2)
);

                
/*__________Ejercicio 23__________
Nombre y apellido de los actores que no han actuado en ninguna película de
la categoría "Horror". Utiliza una subconsulta para encontrar los actores que han actuado
en películas de la categoría "Horror" y luego exclúyelos de la lista de actores.*/ 

SELECT a.first_name, a.last_name
FROM actor a
WHERE a.actor_id NOT IN (
    SELECT fa.actor_id
    FROM film_actor fa
    JOIN inventory i ON fa.film_id = i.film_id
    JOIN film_category fc ON fa.film_id = fc.film_id
    JOIN category c ON fc.category_id = c.category_id
    WHERE c.name = 'Horror'
);


/*____________BONUS____________*/ 
             
/*__________Ejercicio 24__________
BONUS: Título de las películas que son comedias y tienen una duración mayor a 180 minutos (tabla film).*/ 
 
SELECT f.title
FROM film f
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c ON fc.category_id = c.category_id
WHERE c.name = 'Comedy' AND f.length > 180;


/*__________Ejercicio 25__________
Todos los actores que han actuado juntos en al menos una película. Muestra el nombre y apellido de los actores y el número de películas en las
que han actuado juntos.*/ 

SELECT a1.first_name AS actor1_first_name, a1.last_name AS actor1_last_name,
       a2.first_name AS actor2_first_name, a2.last_name AS actor2_last_name,
       joint_films.film_count
FROM actor a1
JOIN (
    SELECT fa1.actor_id AS actor1_id, fa2.actor_id AS actor2_id, COUNT(*) AS film_count
    FROM film_actor fa1
    JOIN film_actor fa2 ON fa1.film_id = fa2.film_id AND fa1.actor_id < fa2.actor_id
    GROUP BY fa1.actor_id, fa2.actor_id
) AS joint_films ON a1.actor_id = joint_films.actor1_id
JOIN actor a2 ON joint_films.actor2_id = a2.actor_id
ORDER BY film_count DESC, actor1_last_name, actor1_first_name, actor2_last_name, actor2_first_name;

