DROP TABLE IF EXISTS STUDENT;
CREATE TABLE IF NOT EXISTS STUDENT (
    ROLL_NO TEXT PRIMARY KEY,
    NAME TEXT NOT NULL,
    ADDRESS TEXT,
    PHONE TEXT,
    AGE INTEGER
);

INSERT INTO STUDENT (ROLL_NO, NAME, ADDRESS, PHONE, AGE) VALUES
('1', 'Micheal', 'New York', '**', 19 ),
('2', 'Joe', 'Edison', '**', 16 ),
('3', 'Billy', 'New York', '**', 23 ),
('4', 'Bob', 'Seattle', '**', 19 ),
('5', 'Max', 'Oklahoma', '**', 21 );


SELECT * FROM STUDENT;


SELECT * FROM STUDENT
WHERE NAME = 'Micheal' AND ADDRESS = 'New York';
SELECT * FROM STUDENT
WHERE AGE = 19 AND NAME = 'Bob';
SELECT * FROM STUDENT
WHERE NAME='Bob' OR AGE = 19;
SELECT * FROM STUDENT
WHERE AGE = 16 AND (NAME='Joe' OR NAME = 'Bob');