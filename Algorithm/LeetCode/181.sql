-- 181. Employees Earning More Than Their Managers
-- Write an SQL query to find the employees who earn more than their managers.
-- Return the result table in any order.

SELECT name AS Employee
FROM Employee A
WHERE A.salary > (SELECT B.salary 
                FROM Employee B
                WHERE A.managerId = B.id);

-- self join으로 같은 테이블 내에 있는 컬럼들을 연결해준다. 