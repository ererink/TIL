SELECT COUNT(*) AS '고객 수' FROM customers;

SELECT FirstName AS '이름', LastName AS '성' 
FROM customers
WHERE Country = 'USA'
ORDER BY FirstName;

SELECT COUNT(*) AS '송장 수'
FROM invoices
WHERE BillingPostalCode != 'NULL';

SELECT * 
FROM invoices
WHERE BillingState ISNULL
ORDER BY InvoiceDate DESC 
LIMIT 5;

SELECT COUNT(*) 
FROM invoices
WHERE strftime('%Y', InvoiceDate) = '2013';

SELECT CustomerId AS '고객ID', FirstName AS '이름', LastName AS '성'
FROM customers
WHERE FirstName LIKE 'L%'
ORDER BY CustomerId;

SELECT Country AS '나라', COUNT(*) AS '고객 수'
FROM customers
GROUP BY Country
ORDER BY COUNT(*) DESC
LIMIT 5;

SELECT ArtistId, COUNT(ArtistId) AS '앨범 수'
FROM albums
ORDER BY COUNT(ArtistId) 
LIMIT 1;

SELECT ArtistId, COUNT(*) AS '앨범 수'
FROM albums
GROUP BY ArtistId
HAVING COUNT(*) >= 10
ORDER BY COUNT(*) DESC;

SELECT Country, State, COUNT(State) AS '고객 수' 
FROM customers
GROUP BY Country, State
HAVING State != 'NULL'
ORDER BY COUNT(State) DESC 
LIMIT 5;

SELECT CustomerId,
    CASE
        WHEN Fax ISNULL THEN 'X'
        ELSE 'O'
    END AS 'Fax 유/무' 
FROM customers
ORDER BY CustomerId
LIMIT 5;

SELECT LastName, FirstName, strftime('%Y/%m/%d','now')- strftime('%Y', BirthDate) + 1 AS "나이"
FROM employees
ORDER BY EmployeeId;

SELECT Name
FROM artists
WHERE ArtistId = (SELECT ArtistId
    FROM albums
    GROUP BY ArtistId
    ORDER BY COUNT(*) DESC
    LIMIT 1);

SELECT Name
FROM genres
WHERE GenreId = (SELECT GenreId
    FROM tracks 
    GROUP BY GenreId 
    ORDER BY COUNT(*)
    LIMIT 1);