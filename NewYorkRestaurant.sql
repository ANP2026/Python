CREATE TABLE IF NOT EXISTS Restaurant (
    name TEXT,
    neighboorhood TEXT,
    cuisine TEXT,
    review REAL,
    price TEXT,
    health TEXT
);
INSERT INTO Restaurant(name, neighboorhood, cuisine, review, price, health) VALUES
('Peter', 'Brooklyn', 'Steak', 4.4, '$$$$', 'A'),
('Jongro', 'Midtown', 'Korean', 3.5, '$$', 'A'),
('Pocha', 'Midtown', 'Pizza', 4.0, '$$$', 'B'),
('Lighthouse', 'Queens', 'Chinese', 3.9, '$', 'A'),
('Minca', 'Downtown', 'American', 4.6, '$$$', ''),
('Marea', 'Chinatown', 'Chinese', 3.0, '$$', ''),
('Dirty Candy', 'Uptown', 'Italian', 4.9, '$$$$', 'B'),
('Di Fara Pizza', 'Brooklyn', 'Pizza', 3.8, '$$', 'A'),
('Golden Unicorn', 'Uptown', 'Italian', 3.8, '$$', 'A');
SELECT * FROM Restaurant;
SELECT DISTINCT neighboorhood FROM Restaurant;
SELECT DISTINCT cuisine FROM Restaurant;
SELECT * FROM Restaurant WHERE cuisine = "Chinese";
SELECT * FROM Restaurant WHERE review >= 4;
SELECT * FROM Restaurant WHERE cuisine = "Italian" AND price = "$$$";
SELECT * FROM Restaurant WHERE name LIKE "%Candy";
SELECT * FROM Restaurant WHERE neighboorhood IN("Midtown", "Downtown", "Chinatown");
SELECT * FROM Restaurant WHERE health = "";
SELECT * FROM Restaurant ORDER BY review DESC LIMIT 4;
