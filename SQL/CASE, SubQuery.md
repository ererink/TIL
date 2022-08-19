# CASE

* 특정 상황에서 데이터를 변환하여 활용할 수 있다. 

* ELSE를 생략하는 경우 NULL값이 지정된다. 

* 조건문과 같은 역할을 한다.

```sql
CASE
    WHEN 조건식 THEN 식
    WHEN 조건식 THEN 식
    ELSE 식
END
```

### 예문

gender가 1일때 남자를, 2일때 여자를 출력해보자. 

```sql
SELECT
    id,
    CASE
        WHEN gender = 1 THEN '남자'
        WHEN gender = 2 THEN '여자'
    END AS 성별
FROM healthcare
LIMIT 5;

-- id  성별
-- --  -----
-- 1   남자
-- 2   여자
-- 3   여자
-- 4   남자
-- 5   여자
```

CASE는 찾고자하는 컬럼 뒤, SELECT절에 조건을 달아 찾도록 한다. 

나이에 따라 청소년(~18), 청년(~30), 중장년(~64)로 출력한다. 

```sql
SELECT 
    first_name,
    last_name,
    age,
    CASE 
        WHEN age <= 18 THEN '청소년'
        WHEN age <= 40 THEN '청년'
        WHEN age <= 90 THEN '중장년'
        ELSE '노년' 
    END
FROM users
LIMIT 10;
```

CASE절에서 비교 연산자와 함께 각 나이에 맞는 조건을 달아준다. 

# 서브쿼리

* 특정한 값을 **메인 쿼리에 반환**하여 활용하는 것이다. 

* **테이블에 없는 기준**을 이용한 검색이 가능하다. 

* 서브 쿼리는 **소괄호**로 감싸서 사용하며, 메인 쿼리의 칼럼을 모두 사용할 수 있다. 

* **메인 쿼리는 서브 쿼리의 칼럼을 이용할 수 없다.**

## 단일행 서브쿼리

* 서브쿼리의 결과가 0 또는 1개인 경우

* 단일행 **비교 연산자**와 함께 사용한다. 
  
  * =, <, <=, >=, >, <>

users에서 가장 나이가 작은 사람의 수를 출력한다. 

```sql
SELECT age, COUNT(*)
FROM users
GROUP BY age
ORDER BY age
LIMIT 1; 


-- age  COUNT(*)
-- ---  --------
-- 15   39
```

모든 데이터를 정렬하여 제일 작은 수를 찾고, 해당 데이터와 같은 데이터를 카운트한다. 

```sql
SELECT MIN(age) 
FROM users;
-- MIN(age)
-- --------
-- 15

SELECT COUNT(*)
FROM users 
WHERE age = 15;
-- COUNT(*)
-- --------
-- 39
```

MIN()과 WHERE절에서 'age = 15'를 사용하는 것과 같다. 

```sql
SELECT COUNT(*)
FROM users 
WHERE age = (SELECT MIN(age) FROM users); 

-- COUNT(*)
-- --------
-- 39
```

위 구문을 서브쿼리로 작성할 수 있다. 

WHERE절에서 'age ='과 함께 users 테이블의 가장 작은 나이의 데이터를 조회하는 것을 조건으로 즉, 서브쿼리로 활용하여 데이터를 조회한다.  

users에서 평균 계좌 잔고가 높은 사람의 수를 출력한다. 

```sql
SELECT COUNT(*)
FROM users
WHERE balance > (SELECT AVG(balance) FROM users);  


-- COUNT(*)
-- --------
-- 222
```

users에 존재하는 모든 잔액의 평균과 비교하여 데이터를 조회한다. 

users에서 유은정과 같은 지역에 사는 사람의 수를 출력한다. 

```sql
SELECT 
    COUNT(*)
FROM users
WHERE country = (SELECT country FROM users
WHERE last_name = '유' AND first_name = '은정');
```

WHERE절에서 서브쿼리로 '유은정'의 조건을 넣고 이를 country에서 찾도록 한다. 

#### UPDATE 활용 set

```sql
UPDATE users
SET balance = (SELECT AVG(balance) FROM users);
```

모든 사람들의 balance를 평균 잔고로 똑같이 바꾼다.

## 다중행 서브쿼리

* 서브쿼리 결과가 2개 이상인 경우

* 다중행 비교 연산자와 함께 사용한다. 
  
  * **IN, EXISTS**등

users에서 이은정과 같은 지역에 사는 사람의 수를 출력한다. 

```sql
SELECT 
    country
FROM users
WHERE last_name = '이' AND first_name = '은정'; 

-- country
-- -------
-- 전라북도
-- 경상북도
```

'유은정'과 같은 지역의 사람들의 인원수를 구하는 단일행 서브쿼리와 같은 구문을 사용할 수 없다. 

위 구문을 통해 알 수 있듯이 '이은정'은 총 2명이며, 각 이은정들은 전라북도와 경상북도의 데이터를 가지고 있다. 

```sql
SELECT 
    COUNT(*)
FROM users
WHERE country = (SELECT country FROM users
WHERE last_name = '이' AND first_name = '은정');  

-- COUNT(*)
-- --------
-- 115
```

그리하여 위의 '유은정' 조회 구문과 같이 작성한다면 115의 값이 출력된다. 

```sql
SELECT country, COUNT(*)
FROM users
GROUP BY country;
-- country  COUNT(*)
-- -------  --------
-- 강원도      101
-- 경기도      114
-- 경상남도     106
-- 경상북도     103
-- 전라남도     123
-- 전라북도     115
-- 제주특별자치도  118
-- 충청남도     105
-- 충청북도     115
```

이는 첫 번째 이은정의 country인 '전라북도'의 값만 나온 것이다. 

모든 이은정의 country의 사람 수를 출력하기 위해서는 다중행 서브쿼리를 이용해야 한다. 

```sql
SELECT 
    COUNT(*)
FROM users
WHERE country IN (SELECT country FROM users
WHERE last_name = '이' AND first_name = '은정');  


-- COUNT(*)
-- --------
-- 218
```

**IN**을 통해 모든 이은정이 포함된 지역의 사람 수를 출력할 수 있다. 

전라북도 (115) + 경상북도(103)을 더한 사람의 수가 출력된다. 

특정 성씨에서 가장 어린 사람들의 이름과 나이를 출력한다. 

```sql
SELECT
    last_name,
    first_name,
    age
FROM users
WHERE (last_name, age) IN (
    SELECT 
        last_name,
        MIN(age)
    FROM users
    GROUP BY last_name)
ORDER BY last_name;
```

IN을 통해 last_name으로 그룹을 만들고, last_name을 기준으로 정렬하여 이 그룹 안에서 가장 어린 나이(MIN(age))와 성을 조회한다. 

최종적으로 그룹의 last name, first name, age를 출력한다. 
