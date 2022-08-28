-- 182. Duplicate Emails
-- Write an SQL query to report all the duplicate emails.
-- Return the result table in any order.

SELECT email AS Email
FROM Person
GROUP BY email
HAVING COUNT(email) >= 2;