-- Exercícios 3:

-- a)
SELECT
	employees.name nome,
	employees.role cargo,
	departments.name departamento
FROM employees
INNER JOIN departments
ON employees.department_id = departments.id;

SELECT
	e.name nome,
	e.role cargo,
	d.name departamento
FROM employees e
INNER JOIN departments d
ON e.department_id = d.id;

-- b) Selecione o nome, o cargo e o salário dos funcionários do departamento de vendas.
SELECT
	e.name nome,
	e.role cargo,
	e.salary salário,
	d.name departamento
FROM employees e
INNER JOIN departments d
ON e.department_id = d.id
WHERE d.name ILIKE 'vendas';

-- c)Selecione o nome, o cargo e o salário dos funcionários cujo salário seja maior que 3500 e que trabalham no departamento de vendas.
SELECT
	e.name nome,
	e.role cargo,
	e.salary salário,
	d.name departamento
FROM employees e
INNER JOIN departments d
ON e.department_id = d.id
WHERE e.salary::numeric > 3500 AND d.name ILIKE 'vendas';

-- d)
SELECT
	e.name nome,
	e.role cargo,
	e.salary salário,
	STRING_AGG(p.name, ',') projetos
FROM employees e
INNER JOIN departments d
ON e.department_id = d.id
INNER JOIN projects p
ON p.department_id = d.id
GROUP BY e.id;

-- e)
SELECT SUM(salary::numeric) "Total_Salários" FROM employees;

-- f)
SELECT
	e.name nome,
	e.salary salário,
	d.name departamento
FROM employees e
INNER JOIN departments d
ON e.department_id = d.id;

--  g)
SELECT
	e.salary salário,
	d.name departamento
FROM employees e
INNER JOIN departments d
ON e.department_id = d.id
WHERE MAX(e.salary);