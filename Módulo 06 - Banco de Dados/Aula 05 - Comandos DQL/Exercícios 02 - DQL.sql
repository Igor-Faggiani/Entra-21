-- Exercícios 2:

-- a)
SELECT SUM(quantity_in_stock) AS produtos FROM products;

-- b)
SELECT ROUND(AVG(price::numeric), 2)::money AS "Preço médio dos Produtos" FROM products;

-- c)
SELECT product Produto, MAX(price) "Preço"
FROM products
GROUP BY 1
ORDER BY 2 DESC
LIMIT 1;

-- d)
SELECT product Produto, MIN(price) "Preço"
FROM products
GROUP BY 1
ORDER BY 2 ASC
LIMIT 1;

-- e)
SELECT product, quantity_in_stock, price * quantity_in_stock "Valor_Total"
FROM products
GROUP BY 1, 2, 3
ORDER BY 3;

-- f)
SELECT product, quantity_in_stock 
FROM products 
WHERE quantity_in_stock < 20;

-- g)
SELECT product, price * quantity_in_stock "Valor_Total"
FROM products
GROUP BY 1, 2
ORDER BY 2 DESC
LIMIT 1;