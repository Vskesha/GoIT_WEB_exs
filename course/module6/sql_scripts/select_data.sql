SELECT id, name as fullname
FROM contacts as c 
WHERE favorite != TRUE 
ORDER BY fullname
LIMIT 10;

SELECT name, email 
FROM users u
WHERE age IN (20, 30, 40)
ORDER BY name;

SELECT name, email 
FROM users u
WHERE age BETWEEN 32 and 40
ORDER BY name;

SELECT name, email 
FROM users u
WHERE age >= 32 and age <= 40
ORDER BY name;

SELECT name, email 
FROM contacts c 
WHERE name LIKE "%l%"
ORDER BY name;

SELECT COUNT(user_id) as total, user_id 
FROM contacts c 
GROUP BY user_id;

-- Знайти всі контакти користувачів, молодших за 35 років
SELECT * 
FROM contacts c 
WHERE user_id in (
	SELECT id 
	FROM users 
	WHERE age < 35
)
ORDER BY user_id, name;

SELECT *
FROM contacts c 
JOIN users u ON c.user_id == u.id;

SELECT 
	c.name contact_name, 
	c.email contact_email, 
	c.phone contact_phone, 
	u.name user_name, 
	u.email user_email
FROM contacts c 
JOIN users u ON c.user_id == u.id;

SELECT 
	c.name contact_name, 
	c.email contact_email, 
	c.phone contact_phone, 
	u.name user_name, 
	u.email user_email
FROM contacts c 
LEFT JOIN users u ON c.user_id == u.id;

SELECT 
	c.name contact_name, 
	c.email contact_email, 
	c.phone contact_phone, 
	u.name user_name, 
	u.email user_email
FROM contacts c 
RIGHT JOIN users u ON c.user_id == u.id;

SELECT 
	c.name contact_name, 
	c.email contact_email, 
	c.phone contact_phone, 
	u.name user_name, 
	u.email user_email
FROM contacts c 
FULL JOIN users u ON c.user_id == u.id;

UPDATE contacts SET user_id = 3 WHERE id = 5;

CREATE INDEX idx_name ON contacts (name);
DROP INDEX idx_name;