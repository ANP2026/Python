CREATE TABLE IF NOT EXISTS students (
    name TEXT,
    grade TEXT,
    age TEXT,
    city TEXT
);
INSERT INTO students(name, grade, age, city) VALUES
("Max", "7", "12", "Edison"),
("Jay", "5", "10", "New York"),
("Bob", "9", "15", "Seattle");
SELECT * FROM students;
SELECT name, city FROM students where city = "New York";
