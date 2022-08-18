# 기본 함수와 연산

## 문자열 함수

* SUBSTR(문자열, start, length)
  
  * 문자열 자르기
  
  * 시작 인덱스는 1, 마지막 인덱스는 -1

* TRIM(문자열), LTRIN, RTRIM
  
  * 문자열 공백 제거 

* LENGTH(문자열)
  
  * 문자열 길이

```sql
SELECT LENGTH(first_name), firtst_name FROM users LIMIT 5;
```

      ↳ 문자열 길이를 반환한다.

* REPLACE(문자열, 패턴, 변경값)
  
  * 패턴에 일치하는 부분을 변경한다. 

```sql
SELECT firtst_name REPLACE(phone, '-', '') FROM users LIMIT 5;
```

    ↳ REPLACE: 전화번호의 '-'를 모두 없앤다.

* UPPER(문자열), LOWER
  
  * 대소문자 변경

* ||
  
  * 문자열 합치기 (concatenation)

```sql
SELECT last_name || first_name FROM USERS LIMIT5;
```

    ↳ 문자열 합치기: 성과 이름 합치기

## 숫자 함수

* ABS(숫자)
  
  * 절대값

* SIGN(숫자)
  
  * 부호 (양수 1, 음수 -1, 0 0)

* MOD(숫자1, 숫자2)
  
  * 숫자 1을 숫자2로 나눈 **나머지**

```sql
SELECT MOD(5, 2) FROM USERS LIMIT 1;
>>> 1.0
```

* CEIL(숫자), FLOOR(숫자), ROUND(숫자)
  
  * 올림, 내림, 반올림

```sql
SELECT CEIL(3.14), FLOOR(3.14), ROUND(3.14) FROM users LIMIT 1;
>>> 4.0 3.0 3.0
```

* POWER(숫자1, 숫자2)
  
  * 숫자1의 숫자2 제곱

```sql
-- 9^2
SELECT POWER(9, 2) FROM users LIMIT 1;
>>> 81.0
```

* SQRT(숫자)
  
  * 제곱근

```sql
-- 9의 제곱근
SELECT SQRT(9) FROM users LIMIT 1;
>>> 3 
```

# GROUP BY

### Aggregate Function 집계함수

* 값 집합에 대한 계산을 수행하고 **단일 값**을 반환한다. 
  
  * 여러 행으로부터 하나의 결과값을 반환한다. 

* SELECT 구문에서만 사용된다. 
  
  * ex) COUNT(*), AVG(age), etc. 

### ALIAS

* 칼럼명이나 테이블명을 다른 명칭으로 확인하고 싶을 때 활용한다. 

* AS를 생략하여 공백으로 표현할 수 있다. 

* 별칭에 공백, 특수문자 등이 있는 경우 따옴표로 묶어서 표기한다. 

```sql
SELECT last_name 성 FROM users;
SELECT last_name AS 성 FROM users;
SELECT last_name AS 성 FROM users WHERE 성='김';
```

### GROUP BY

* “make a set of summary rows from a set of rows”
  
  * 요약 행 집합을 만든다. 
  
  * 하나 이상의 열 값으로 요약 행으로 만든다. 

* WHERE 절이 포함된 경우 반드시 WHERE절 뒤에 작성해야 한다. 

* 집계함수와 활용하였을 때 의미가 있다. 

* 행을 그룹화하고 각 그룹의 값을 반환한다. 

```sql
SELECT * FROM users GROUP BY last_name;
```

![group by.png](C:\Users\yelki\OneDrive\사진\스크린샷\group%20by.png)

(((((((DISTINCT 아님!))))))))

```sql
SELECT last_name, COUNT(*) FROM users GROUP BY last_name;
```

    ↳ user에서 각 성씨가 몇 명씩 있는지 조회한다. 

* GROUP BY에서 활용하는 컬럼을 제외하고는 **집계함수**를 써야한다. 

```sql
SELECT last_name, age, COUNT(*)
FROM users
GROUP BY last_name;
```

이 구문에서 SELECT 절에 age를 추가하면 (GROUP BY에 해당하지 않은 컬럼) 

해당하는 성씨의 첫번째 행에 있는 나이가 출력되기 때문에 (걍 아무 의미없는 출력값) 그룹화한 값들과 비교했을 때 아무 의미가 없다. 

```sql
SELECT last_name, AVG(age), COUNT(*)
FROM users
GROUP BY last_name;
```

그러므로 AVG(age)와 같은 집계함수를 사용하여 GROUP BY에 맞는 출력값을 출력하도록 한다. 

* GROUP BY의 결과는 정렬되지 않는다. 
  
  * 기존의 출력한 순서와 추후에 출력한 출력값이 다를 수 있다. 
  
  * 정렬은 무조건 ORDER BY를 사용한다. 

* GROUP BY WHERE 사용

100명 이상의 성만 출력해보자. 

```sql
SELECT last_name, COUNT(last_name)
FROM users
WHERE COUNT(last_name) > 100
GROUP BY last_name;
```

GROUP BY절 전에 조건을 달기 위해 WHERE절을 사용한다. 

이 경우 오류가 발생한다. 

WHERE에서 GROUP BY를 통해 그룹화가 되지 않았기 때문에 출력에 오류가 발생한다.  

따라서, 조건에 따른 GROUP BY를 사용하려면 HAVING을 사용해야 한다. 

### GROUP BY HAVING

```sql
SELECT last_name, COUNT(last_name)
FROM users
GROUP BY last_name
HAVING COUNT(last_name) > 100;
```

* 집계함수는 실행 순서에 의해 WHERE 절의 조건식에서는 사용할 수 없다. 

* 집계한 결과를 조건에 맞게 출력하기 위해 HAVING을 활용한다. 

## SELECT 문자 실행 순서

FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY 

```sql
SELECT 칼럼명
FROM 테이블명
WHERE 조건식
GROUP BY 칼럼 / 표현식
HAVING 그룹 조건식
ORDER BY 칼럼 / 표현식
```

1. FROM: 테이블을 대상으로 

2. WHERE: 제약조건에 밎춰서

3. GROUP BY: 그룹화한다. 

4. HAVING: 그룹 중 조건에 맞는 것만

5. SELECT: 조회하고

6. ORDER BY: 정렬하고

7. LIMIT / OFFSET: 특정 위치값을 가져온다!

# ALTER TABLE

* 이름 변경 -> RENAME

```sql
ALTER TABLE table_name
RENAME TO new_name;
```

* 새로운 컬럼 추가

```sql
ALTER TABLE table_name
ADD COLUMN column_def;
```

* 컬럼 이름 수정

```sql
ALTER TABLE table_name
RENAME COLUMN current_name TO new_name;
```

* 컬럼 삭제 

```sql
ALTER TABLE table_name
DROP COLUMN column_name;
```

#### 

#### DROP  / TRUNCATE / DROP의 차이

* DROP table / column
  
  * 테이블의 전체를 삭제하며, 공간과 객체를 삭제한다. 
  
  * 삭제 후 되돌릴 수 없다. 

* TRUNCATE table / column
  
  * 테이블 자체가 삭제되지 않고, 해당 테이블에 들어있는 모든 행들이 제거되고 저장 공간을 재사용하도록 해제한다. 
  
  * 삭제 후 되돌릴 수 없다. 

* DELETE
  
  * 데이터는 지워지지만 테이블 용량을 줄어들지 않는다. 
  
  * 원하는 데이터만 지울 수 있다. (DROP과 TRUNCATE는 한꺼번에 삭제)
  
  * 삭제 후 되돌릴 수 있다. 

#### 예문

* articles 테이블에 값을 추가하기

```sql
INSERT INTO articles VALUES('#1 title', '#1 content')
```

* 테이블 이름 변경하기

```sql
ALTER TABLE articels RENAME TO new articles;
```

* 새로운 컬럼 추가하기

```sql
ALTER TABLE new articles ADD COLUMN new title TEXT NOT NULL;
```

===> 이 구문에서 오류가 발생하는 이유는

새로운 컬럼 추가 시 기존 레코드에 새로운 컬럼에 대한 정보가 없기 때문에 새로운 컬럼에 레코드를 넣을 수 없다. 

그러므로 컬럼 생성 시 레코드 없이 빈칸으로 생성되고, NOT NULL로 설정하였기 때문에 빈칸으로 둘 수 없어 오류가 나는 것이다. 

오류를 해결하기 위해서는 기본값(DEFAULT)를 설정해야 한다. 
