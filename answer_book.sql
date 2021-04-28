
-- =================================================
--   CS1106/CS6503 Test -- Wednesday, 18 Nov 2020
-- =================================================

-- Your Name: Dylan Forde
-- Your Id: 120309116
-- =================================================
-- QUESTION 1: Place SQL below the dashed line
-- -------------------------------------------------
SELECT first_name, last_name
FROM persons
WHERE first_name LIKE '%r%' OR last_name LIKE '%r%';
-- =================================================
-- QUESTION 2: Place SQL below the dashed line
-- -------------------------------------------------
SELECT county, COUNT(first_name)
FROM persons 
GROUP BY county
ORDER BY county ASC;
-- =================================================
-- QUESTION 3: Place SQL below the dashed line
-- -------------------------------------------------
SELECT first_name AS 'first name', last_name AS 'last name' , food AS 'favourite foods'
FROM persons
JOIN likes
ON persons.person_id = likes.person_id
WHERE food LIKE '%e%'
GROUP BY first_name;
-- =================================================
-- QUESTION 4: Place SQL below the dashed line
-- -------------------------------------------------
SELECT p1.person_id AS 'Personal ID' , p1.first_name AS 'First Name', p1.last_name AS 'Last Name' , 'is friends with' AS 'is friends with:' , p2.first_name AS 'Friends First Name'
FROM persons AS p1
JOIN knows
ON p1.person_id = knows.person_id
JOIN persons AS p2
ON friend_id = p2.person_id
WHERE p1.first_name LIKE 'Aoife';
-- =================================================
-- QUESTION 5: Place SQL below the dashed line
-- -------------------------------------------------
SELECT p1.person_id AS 'Personal ID' , p1.first_name AS 'First Name', p1.last_name AS 'Last Name' , 'is friends with' AS 'is friends with:' , p2.first_name AS 'Friends First Name'
FROM persons AS p1
JOIN knows
ON p1.person_id = knows.person_id
JOIN persons AS p2
ON friend_id = p2.person_id
EXCEPT
SELECT p1.person_id AS 'Personal ID' , p1.first_name AS 'First Name', p1.last_name AS 'Last Name' , 'is friends with' AS 'is friends with:' , p2.first_name AS 'Friends First Name'
FROM persons AS p1
JOIN knows
ON p1.person_id = knows.person_id
JOIN persons AS p2
ON friend_id = p2.person_id
WHERE p1.first_name LIKE 'Aoife' OR p2.first_name LIKE 'Aoife';
-- =================================================
-- QUESTION 6: Place SQL below the dashed line
-- -------------------------------------------------
SELECT p1.person_id AS 'Personal ID' , p1.first_name AS 'First Name', p1.last_name AS 'Last Name' , 'is friends with' AS 'is friends with:' , p2.first_name AS 'Friends First Name'
FROM persons AS p1
JOIN knows 
ON p1.person_id = knows.person_id
JOIN persons AS p2
ON friend_id = p2.person_id
WHERE p2.first_name LIKE 'Declan' AND p2.first_name LIKE 'Aoife'
-- =================================================
-- QUESTION 7: Place SQL below the dashed line
-- -------------------------------------------------
SELECT MIN(birth_date) AS 'oldest', first_name
FROM persons;
SELECT MAX(birth_date) AS 'youngest',first_name
FROM persons;
-- =================================================
-- QUESTION 8: Place SQL below the dashed line
-- -------------------------------------------------
SELECT *
FROM persons
CROSS JOIN likes
ON persons.person_id = likes.person_id
WHERE county LIKE 'Cork'
GROUP BY county
ORDER BY food DESC;
-- =================================================
-- QUESTION 9: Place SQL below the dashed line
-- -------------------------------------------------
SELECT first_name AS 'first name', last_name AS 'last name' , food AS 'favourite foods', county
FROM persons
JOIN likes
ON persons.person_id = likes.person_id
GROUP BY county AND food
HAVING COUNT(food) > 3;
-- =================================================
-- QUESTION 10: Place SQL below the dashed line
-- -------------------------------------------------
SELECT DISTINCT p1.first_name, p1.last_name,p2.first_name, p2.last_name
FROM persons AS p1
JOIN persons AS p2
ON p1.person_id = p2.person_id
WHERE substr(p1.first_name,1,1) = substr(p2.first_name,1,1)
-- This is for all the tables --
SELECT *
FROM knows;
SELECT * 
FROM persons;
SELECT *
FROM likes;