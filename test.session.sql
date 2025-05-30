CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100),
    password VARCHAR(100),
);

-- @block
INSERT INTO users (username, email, password) VALUES ('John Doe', 'john@example.com', 'password123'), ('Jane Doe', 'jane@example.com', 'password456');

-- @block
SELECT * FROM users;

-- @block
ALTER TABLE users
CHANGE password password VARCHAR(50);

-- @block
DELETE FROM users
WHERE id = 12;





