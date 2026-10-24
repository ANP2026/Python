CREATE TABLE IF NOT EXISTS departments(
    department_id TEXT PRIMARY KEY,
    department_name TEXT,
    office_city TEXT,
    department_details TEXT
);
INSERT INTO departments(department_id, department_name, office_city, department_details)
VALUES
("D01","Engineering","New York","Builds and maintains software products"),
("D02","Marketing","Paris","Promotes products and manages customer outreach"),
("D03","Sales","London","Works with customers and grows revenue"),
("D04","Human Resources","Rome","Supports employees and hiring");

CREATE TABLE IF NOT EXISTS employees(
    employee_id TEXT PRIMARY KEY,
    employee_name TEXT,
    city TEXT,
    department_id TEXT,
    job_title TEXT,
    annual_salary REAL
);
INSERT INTO employees(employee_id, employee_name, city, department_id, job_title, annual_salary)
VALUES
("E5001","James Hoog","New York","D01","Software Engineer",92000),
("E5002","Nail Knite","Paris","D02","Marketing Specialist",68000),
("E5005","Pit Alex","London","D03","Sales Representative",72000),
("E5006","Mc Lyon","Paris","D01","Data Analyst",84000),
("E5007","Paul Adam","Rome","D04","HR Coordinator",65000),
("E5003","Lauson Hen","San Jose","D03","Sales Manager",98000),
("E5008","Ava Patel","New York","D01","Product Manager",105000),
("E5009","Noah Kim","Berlin","D02","Content Writer",61000);

CREATE TABLE IF NOT EXISTS salary_details(
    salary_id TEXT PRIMARY KEY,
    employee_id TEXT,
    pay_date TEXT,
    gross_pay REAL
);
INSERT INTO salary_details(salary_id, employee_id, pay_date, gross_pay)
VALUES
("S70001","E5005","2025-10-05",6000),
("S70009","E5001","2025-09-10",7666.67),
("S70002","E5002","2025-10-05",5666.67),
("S70004","E5003","2025-08-17",8166.67),
("S70007","E5008","2025-09-10",8750),
("S70005","E5006","2025-07-27",7000),
("S70010","E5007","2025-10-05",5416.67),
("S70011","E5009","2025-09-10",5083.33);

-- Employee salaries and roles
SELECT employee_name AS "Employee",
       job_title AS "What They Do",
       annual_salary AS "Annual Salary"
FROM employees;

-- Salary payment details
SELECT employees.employee_name AS "Employee",
       salary_details.pay_date AS "Pay Date",
       salary_details.gross_pay AS "Gross Pay"
FROM salary_details
JOIN employees ON salary_details.employee_id = employees.employee_id;

-- Employees earning at least $70,000
SELECT employee_name AS "Employee",
       annual_salary AS "Annual Salary"
FROM employees
WHERE annual_salary >= 70000;

-- Payments made on October 5, 2025
SELECT employees.employee_name AS "Employee",
       salary_details.gross_pay AS "Gross Pay"
FROM salary_details
JOIN employees ON salary_details.employee_id = employees.employee_id
WHERE salary_details.pay_date = "2025-10-05";
