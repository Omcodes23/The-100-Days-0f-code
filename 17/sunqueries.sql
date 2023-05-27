-- Using a Subquery --
SELECT last_name
FROM employees
WHERE salary > (SELECT salary
                FROM employees
                WHERE last_name = 'Abel');

-- Single-Row Subqueries --
SELECT last_name, job_id
FROM employees
WHERE job_id =(SELECT job_id
                FROM employees
                WHERE employee_id = 141);

SELECT last_name, job_id, salary
FROM employees
WHERE job_id = (SELECT job_id
                FROM employees
                WHERE employee_id = 141)
AND salary >(SELECT salary
                FROM employees
                WHERE employee_id = 143);

-- Using Group Functions in a Subquery --
SELECT last_name, job_id, salary
FROM employees
WHERE salary = (SELECT MIN(salary)
                FROM employees);


-- The HAVING Clause with Subqueries --
SELECT department_id, MIN(salary)
FROM employees
GROUP BY department_id
HAVING MIN(salary) > (SELECT MIN(salary)
                        FROM employees
                        WHERE department_id = 50);


-- Multiple-Row Subqueries --
SELECT last_name, salary, department_id
FROM employees
WHERE salary IN (SELECT MIN(salary)
FROM employees
GROUP BY department_id);

-- Using the ANY Operator --
-- in Multiple-Row Subqueries --
SELECT employee_id, last_name, job_id, salary
FROM employees
WHERE salary < ANY (SELECT salary
                    FROM employees
                    WHERE job_id = 'IT_PROG')
AND job_id <> 'IT_PROG';

-- Null Values in a Subquery --
SELECT emp.last_name
FROM employees emp
WHERE emp.employee_id NOT IN (SELECT mgr.manager_id
FROM employees mgr);

SELECT last_name FROM employees
WHERE employee_id NOT IN (SELECT manager_id FROM employees
WHERE manager_id IS NOT NULL);

