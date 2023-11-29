-- Exercícios 1:

-- a)
SELECT title, author FROM books;

-- b)
SELECT title, author FROM books WHERE author LIKE 'Henry Davis';

-- c)
SELECT title, author, release_year FROM books WHERE release_year < 1900;

-- d)
SELECT title FROM books WHERE title LIKE 'O%';

-- e)
SELECT title, author FROM books WHERE release_year > 1950;

-- f)
SELECT COUNT(title) FROM books;

-- g)
SELECT author, COUNT(*) "Quatidade de Livros Publicados"
FROM books
GROUP BY 1
ORDER BY 2 DESC
LIMIT 1;

-- h)
SELECT title, release_year FROM books ORDER BY 2 ASC;

-- i)
SELECT title, release_year 
FROM books 
ORDER BY 2 ASC
LIMIT 1;

-- j)
SELECT title, release_year
FROM books
ORDER BY 2 DESC
LIMIT 1;

-- k)
SELECT title, author
FROM books
ORDER BY id DESC
LIMIT 3;