SET lc_monetary = 'pt_BR';

-- Selecionando todas as colunas
SELECT * FROM employees;

-- Selecionando colunas em específico
SELECT name, age FROM employees;

-- Definindo um limite para a consulta
SELECT * FROM employees LIMIT 5;

-- Definindo um início para a consulta
SELECT * FROM employees LIMIT 5 OFFSET 3;

-- Selecionando os dados com condições (<> Sinal de diferente)
SELECT * FROM employees WHERE age > 30;

-- Between --> Intervalo de valores
SELECT * FROM employees WHERE age BETWEEN 20 AND 25;

-- Casting --> Conversão de tipo de dado
SELECT * FROM employees WHERE salary BETWEEN 'R$ 300' AND 'R$ 7000';

SELECT * FROM employees WHERE CAST(salary AS numeric) BETWEEN 3000 AND 7000;

SELECT * FROM employees WHERE salary::numeric BETWEEN 300 AND 7000;

-- Operador IN
SELECT * FROM employees WHERE age in (27, 29, 41);

-- Operador LIKE
SELECT * FROM employees WHERE name LIKE 'Ig%';

SELECT * FROM employees WHERE name ILIKE '%ig%';

SELECT * FROM employees WHERE name ILIKE '%re__';

-- INNER JOIN - Seleciona a intersecção entre as duas tabelas
SELECT employees.name, departments.name
FROM employees
INNER JOIN departments
ON employees.department_id = departments.id;

-- Definindo apelidos para as colunas
SELECT e.name AS "Funcionário", d.name AS "Departamento"
FROM employees AS e
INNER JOIN departments AS d
ON e.department_id = d.id;

-- LEFT JOIN
SELECT e.name AS funcionário, d.name AS departamento
FROM employees AS e
LEFT JOIN departments d
ON e.department_id = d.id;

-- RIGHT JOIN
SELECT e.name AS funcionário, d.name AS departamento
FROM employees AS e
RIGHT JOIN departments d
ON e.department_id = d.id;

-- FULL JOIN
SELECT e.name AS funcionário, d.name AS departamento
FROM employees AS e
FULL JOIN departments d
ON e.department_id = d.id;

-- Funções Agregadoras

-- COUNT --> Conta as ocorrências
SELECT COUNT(*) FROM employees;

SELECT COUNT(*) FROM employees WHERE salary::numeric > 3000;

-- MAX -->  Maior ocorrência
SELECT MAX(salary) FROM employees;

-- MIN --> Menor valor
SELECT MIN(salary) FROM employees;

-- SUM --> Soma dos valores
SELECT SUM(salary) FROM employees;

-- AVG --> Média dos valores
SELECT AVG(salary::numeric) FROM employees;

-- ROUND --> Arredonar casas decimais
SELECT ROUND(AVG(salary::numeric), 2) FROM employees;

-- GROUP BY --> Agrupar colunas
SELECT department_id AS "ID do departamento", COUNT(*) AS "Qantidade de funcionários"
FROM employees
GROUP BY 1;

-- COALESCE --> Verifica se a coluna possui valor, caso não possuir, mostra um valor padrão
SELECT
	COALESCE(department_id::text, 'funcionários sem Departamento') AS "ID do departamento", 
	COUNT(*) AS "Qantidade de funcionários"
FROM employees
GROUP BY 1;

-- Com LEFT JOIN
SELECT
	COALESCE(department_id::text, 'funcionários sem Departamento') AS "ID do departamento", 
	COUNT(*) AS "Qantidade de funcionários"
FROM employees e
LEFT JOIN departments AS d
ON e.department_id = d.id
GROUP BY 1;

-- DISTINCT --> Remover as duplicatas da consulta
SELECT DISTINCT(age) FROM employees;

-- ORDER BY --> Ordenar uma ou mais colunas (ASC | DESC)
SELECT DISTINCT(age) FROM employees ORDER BY 1;

-- HAVING --> Filtrar por uma função agregadora
SELECT
	department_id AS "ID do Departamento",
	COUNT(*) "Quantidade de Funcionários"
FROM employees
GROUP BY 1
HAVING COUNT (*) > 3;

-- HAVING usando o INNER JOIN
SELECT 
	d.name AS "Departamento",
	COUNT(*) "Quantidade de Funcionários"
FROM employees as e
INNER JOIN departments d
ON e.department_id = d.id
GROUP BY 1
HAVING COUNT(department_id) > 3;

-- Subconsultas
SELECT name "Funcionário", salary "Salário"
FROM employees
WHERE salary::numeric > (SELECT AVG(salary::numeric) FROM  employees);