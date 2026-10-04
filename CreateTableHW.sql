DROP TABLE IF EXISTS Employees;

CREATE TABLE IF NOT EXISTS Employees (Employee_id TEXT PRIMARY KEY, name TEXT, city TEXT);
INSERT INTO Employees (Employee_id, name, city) VALUES
('5001', 'Eleanor Vance', 'New York'),
('5002', 'Mateo Brooks', 'Paris'),
('5005', 'Priya Sharma', 'London'),
('5006', 'Julian Ross', 'Paris'),
('5007', 'Harper Jenkins', 'Rome'),
('5003', 'Kenji Takahashi', 'San Jose');
SELECT * FROM Employees;
