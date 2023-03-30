 /* emp_id - 사원번호, emp_name - 사원이름, job - 담당업무, dept_id - 부서번호
   sal ,- 급여, bonus - 보너스,  mgr_id - 관리자번호 , hiredate - 입사일*/
SELECT * FROM EMP;

--1. emp 테이블에서 각 사원 emp_name의 급여(sal)에 100을 더한 후 12를 곱한 값이 출력되도록  select절에 산술식을 사용해보세요.(별칭- 년봉 )
SELECT EMP_ID, EMP_NAME, JOB, (SAL + 100) * 12 AS 연봉
FROM EMP;

--2.담당업무 job이 세일즈인 모든 사원의 이름(emp_name), 담당업무(job),부서번호(dept_id)를 검색해 보세요.
SELECT EMP_NAME, JOB, DEPT_ID
FROM EMP
WHERE JOB = '세일즈';

--3.입사일(hiredate)이 “2001년12월3일”인 모든 사원을 검색 하세요.
SELECT EMP_ID, EMP_NAME, JOB, HIREDATE
FROM EMP
WHERE HIREDATE = '2001-12-3';

--4.부서번호(dept_id)가 200인 부서에서 근무하는 모든 사원의 이름과 담당업무,입사일,부서번호검색하세요.
SELECT EMP_NAME, JOB, HIREDATE, DEPT_ID
FROM EMP
WHERE DEPT_ID = 200;

--5.emp테이블에서 급여가 3000이상 5000이하인 모든 사원의 이름과 급여를 출력하세요.
SELECT EMP_NAME, SAL
FROM EMP
WHERE SAL BETWEEN 3000 AND 5000
ORDER BY SAL DESC;

--6.emp테이블에서 관리자번호(mgr_id)가 6311,6361,6351가운데 하나인 모든 사원의 사원번호,관리자번호,이름,부서번호를 출력하세요.
SELECT EMP_ID, MGR_ID, EMP_NAME, DEPT_ID
FROM EMP
WHERE MGR_ID IN (6311,6361,6351);

--7.담당업무가 사무직이거나 경리인 사원의 모든 정보를 검색하세요.
SELECT E.*
FROM EMP E
WHERE JOB IN ('사무직', '경리');

--8.emp테이블에서 급여가 3000이상인 모든 부장의 정보를 검색하세요.
SELECT E.*
FROM EMP E
WHERE SAL >= 3000 AND JOB LIKE '%부장%';

--9. emp테이블에서 담당업무가 세일즈 이거나 사무직이 아닌 모든 사원의 정보를 검색하세요.
SELECT E.*
FROM EMP E
WHERE JOB NOT IN ('세일즈', '사무직');

--10. emp테이블에서 급여가 1500이상 2500이하가  아닌 모든 사원의 정보를 검색하세요.
SELECT E.*
FROM EMP E
WHERE SAL NOT BETWEEN 1500 AND 2500;

--11.담당업무가 경리이거나 부장이면서 급여가 3000이 넘는 모든 사원의 정보를 검색하고 가장먼저 입사한 사람부터 출력하세요.
SELECT E.*
FROM EMP E
WHERE JOB IN ('경리', '부장') AND SAL >= 3000 
ORDER BY HIREDATE;

--12.사원의 부서번호를 기준으로 오름차순으로 정렬하되, 같은 부서 안에서는 급여가 많은 사람이 먼저 출력 되도록 하세요.
SELECT E.*
FROM EMP E
ORDER BY DEPT_ID, SAL DESC;

--13.보너스(bonus)가 null이 아니면서 입사일이 2000년 이상인 사원의 정보를 검색하세요.
SELECT E.*
FROM EMP E
WHERE BONUS IS NOT NULL AND EXTRACT(YEAR FROM HIREDATE) > 2000; 

--14.emp_name이 3글자이고 끝 글자가 ‘수'이며 첫글자는 ’박‘으로 시작하는 사원의 정보검색하세요.
SELECT E.*
FROM EMP E
WHERE LENGTH(EMP_NAME) = 3 AND EMP_NAME LIKE '%수' AND EMP_NAME LIKE '박%';

