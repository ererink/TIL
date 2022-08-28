-- 196. Delete Duplicate Emails
-- Write an SQL query to delete all the duplicate emails, keeping only one unique email with the smallest id. 
-- Note that you are supposed to write a DELETE statement and not a SELECT one.

DELETE A.*
FROM Person A, Person B
WHERE A.email = B.email
    AND A.id > B.id ;

-- self join으로 email과 id를 조회한다. 이때 id가 더 큰 값이 삭제되어야 한다. 