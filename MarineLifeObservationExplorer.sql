CREATE TABLE marine_animal (
animal_id INT PRIMARY KEY,
name VARCHAR(50),
species VARCHAR(50),
weight DECIMAL(10,2),
depth_meters INT,
location VARCHAR(50)
);
INSERT INTO marine_animal(animal_id, name, species,
weight, depth_meters, location) VALUES
(1, 'Blue Whale', 'Mammal', 120000, 200, 'Pacific Ocean'),
(2, 'Dolphin', 'Mammal', 150, 50, 'Indian Ocean'),
(3, 'Great White Shark', 'Fish', 1100, 300, 'Atlantic Ocean'),
(4, 'Clownfish', 'Fish', 0.25, 10, 'Coral Reef'),
(5, 'Green Sea Turtle', 'Reptile', 180, 40, 'Indian Ocean'),
(6, 'Octopus', 'Mollusk', 10, 100, 'Pacific Ocean'),
(7, 'Blue Whale', 'Mammal', 125000, 250, 'Indian Ocean'),
(8, 'Jellyfish', 'Cnidarian', 2, 20, 'Atlantic Ocean'),
(9, 'Sea Horse', 'Fish', 0.2, 15, 'Coral Reef'),
(10, 'Octopus', 'Mollusk', 12, 150, 'Pacific Ocean');
SELECT * FROM marine_animal;
SELECT name FROM marine_animal;
SELECT species FROM marine_animal;
SELECT DISTINCT species AS distinct_species FROM marine_animal;
SELECT COUNT(name) AS total_animals FROM marine_animal;
SELECT SUM(weight) AS total_weight FROM marine_animal;
SELECT AVG(weight) AS avg_weight FROM marine_animal;
