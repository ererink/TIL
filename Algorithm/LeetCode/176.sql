-- Write an SQL query to report the second highest salary from the Employee table. 
-- If there is no second highest salary, the query should report null.

SELECT 
    (SELECT DISTINCT salary 
    FROM Employee
    ORDER BY salary DESC LIMIT 1 OFFSET 1)

AS SecondHighestSalary;

-- 괄호가 존재하지 않으면 해당 table에 값이 1개가 존재할 경우 null을 반환할 수 없다.