CREATE TABLE IF NOT EXISTS salesman(
    salesman_id TEXT PRIMARY KEY,
    name TEXT,
    city TEXT,
    comission TEXT
);
INSERT INTO salesman(salesman_id, name, city, comission) 
VALUES
("5001","James Hoog","New York","0.15"),
("5002","Nail Knite","Paris","0.13"),
("5005","Pit Alex","London","0.11"),
("5006","Mc Lyon","Paris","0.14"),
("5007","Paul Adam","Rome","0.13"),
("5003","Lauson Hen","San Jose","0.12");
CREATE TABLE IF NOT EXISTS customer(
    customer_id TEXT,
    customer_name TEXT PRIMARY KEY,
    customer_city TEXT,
    grade TEXT,
    salesman_id, TEXT
);
INSERT INTO customer(customer_id, customer_name, customer_city, grade, salesman_id) VALUES
("3002","nick rimando","new york","100","5001"),
("3007","brad davis","new york","200","5001"),
("3005","graham zusi","california","200","5002"),
("3008","julian green","london","300","5002"),
("3004","fabian johnson","paris","300","5006"),
("3009","geoff cameron","berlin","100","5003"),
("3003","jozy altidor","moscow","200","5007"),
("3001","brad guzan","london","","5005");
CREATE TABLE IF NOT EXISTS orders(
    ord_no TEXT PRIMARY KEY,
    purch_amt TEXT,
    ord_date TEXT,
    customer_id TEXT,
    salesman_id TEXT
);
INSERT INTO orders(ord_no, purch_amt, ord_date, customer_id, salesman_id) VALUES
("70001","150.5","2012-10-05","3005","5002"),
("70009","270.65","2012-09-10","3001","5001"),
("70002","65.26","2012-10-05","3002","5003"),
("70004","110.5","2012-08-17","3009","5007"),
("70007","948.5","2012-09-10","3005","5005"),
("70005","2400.6","2012-07-27","3007","5006");
SELECT * FROM salesman;
SELECT * FROM customer;
SELECT * FROM orders;

SELECT customer.customer_name, salesman.name, salesman.city
FROM customer
JOIN salesman ON customer.customer_city = salesman.city;

SELECT customer.customer_name, salesman.name
FROM customer
JOIN salesman ON customer.salesman_id = salesman.salesman_id;

SELECT orders.ord_no, customer.customer_name, orders.customer_id, orders.salesman_id
FROM orders
JOIN customer ON orders.customer_id = customer.customer_id
JOIN salesman ON orders.salesman_id = salesman.salesman_id
WHERE customer.customer_city <> salesman.city;

SELECT orders.ord_no, customer.customer_name
FROM orders
JOIN  customer ON orders.customer_id = customer.customer_id;

SELECT customer.customer_name AS "Customer", customer.grade AS "Grade"
FROM orders
JOIN salesman ON orders.salesman_id = salesman.salesman_id
JOIN customer ON orders.customer_id = customer.customer_id
WHERE customer.grade IS NOT NULL;

SELECT customer.customer_name AS "Customer", customer.customer_city AS "City", salesman.name AS "Salesman", salesman.comission
FROM customer
JOIN salesman ON customer.salesman_id = salesman.salesman_id
WHERE salesman.comission BETWEEN 0.12 AND 0.14;

SELECT orders.ord_no, customer.customer_name, salesman.comission AS "Comission%",
orders.purch_amt * salesman.comission AS "Comission"
FROM orders
JOIN salesman ON orders.salesman_id = salesman.salesman_id
Join customer on orders.customer_id = customer.customer_id
WHERE customer.grade >=200;

SELECT *
FROM customer
JOIN orders ON customer.customer_id = orders.customer_id
WHERE orders.ord_date = "2012-10-05";
