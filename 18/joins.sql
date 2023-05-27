-- Oracle joins --
-- Retrieving Records --
-- with Equijoins --
SELECT employees.employee_id,
       employees.last_name,
       employees.department_id,
       departments.department_id,
       departments.location_id
FROM employees, departments
WHERE employees.department_id = departments.department_id;

-- Additional Search Conditions --
-- Using the AND Operator --
SELECT last_name,
       employees.department_id,
       department_name
FROM employees, departments
WHERE employees.department_id = departments.department_id
AND last_name = 'Matos';

-- Using Table Aliases --
SELECT e.employee_id,
       e.last_name,
       e.department_id,
       d.department_id,
       d.location_id
FROM employees e, departments d
WHERE e.department_id = d.department_id;

-- Joining More than Two Tables --
SELECT e.last_name, d.department_name, l.city
FROM employees e, departments d, locations l
WHERE e.department_id = d.department_id
AND d.location_id = l.location_id;

-- Nonequijoins --
SELECT e.last_name, e.salary, j.grade_level
FROM employees e, job_grades j
WHERE e.salary BETWEEN j.lowest_sal AND j.highest_sal;

-- Outer Joins --
SELECT e.last_name, e.department_id, d.department_name
FROM employees e, departments d
WHERE e.department_id = d.department_id;

SELECT e.last_name, e.department_id, d.department_name
FROM employees e, departments d
WHERE e.department_id(+) = d.department_id;

-- Self Joins --
SELECT worker.last_name || ' works for ' || manager.last_name
FROM employees worker, employees manager
WHERE worker.manager_id = manager.employee_id;

-- sql joins --

-- Creating Cross Joins --
SELECT last_name, department_name
FROM employees
CROSS JOIN departments;

-- Creating Natural Joins --
SELECT department_id, department_name,
location_id, city
FROM departments
NATURAL JOIN locations;

-- Creating Joins with the USING Clause --  
SELECT e.employee_id, e.last_name, d.location_id
FROM employees e JOIN departments d
USING (department_id);

-- Creating Joins with the ON Claus --
SELECT e.employee_id, e.last_name, e.department_id,
d.department_id, d.location_id
FROM employees e JOIN departments d
ON (e.department_id = d.department_id);

-- Creating Three-Way Joins with the ON Claus --
SELECT employee_id, city, department_name
FROM employees e
JOIN departments d
ON d.department_id = e.department_id
JOIN locations l
ON d.location_id = l.location_id;

-- INNER versus OUTER Joins --
-- LEFT OUTER JOIN --
SELECT e.last_name, e.department_id, d.department_name
FROM employees e
LEFT OUTER JOIN departments d
ON (e.department_id = d.department_id);

-- RIGHT OUTER JOIN --
SELECT e.last_name, e.department_id, d.department_name
FROM employees e
RIGHT OUTER JOIN departments d
ON (e.department_id = d.department_id);

-- FULL OUTER JOIN --
SELECT e.last_name, e.department_id, d.department_name
FROM employees e
FULL OUTER JOIN departments d
ON (e.department_id = d.department_id);

-- Additional Conditions --
SELECT e.employee_id, e.last_name, e.department_id,
d.department_id, d.location_id
FROM employees e JOIN departments d
ON (e.department_id = d.department_id)
AND e.manager_id = 149;  