# WHERE절 탐색 조건

## WHERE 절에서 사용할 수 있는 연산자

### 비교 연산자

* =, > , >=, <, <=

* 숫자 / 문자 값의 대 / 소, 동일 여부를 확인

### 논리 연산자

* AND
  
  * 앞쪽의 조건과 뒤쪽의 조건 모두 참인 경우

* OR
  
  * 앞쪽의 조건 혹은 뒤쪽의 조건 중 둘 중 하나가 참인 경우

* NOT
  
  * 뒤에 오는 조건의 결과가 반대인 경우 

## 기타 연산자

### BETWEEN  값1 AND 값2

* 값 1과 값 2 사이의 값을 비교

* (값1 <= 비교값 <= 값2)

### IN(값1, 값2, ...)

* 목록 중 값이 하나라도 일치할 경우

### LIKE

* 비교 문자열과 **형태**가 일치한 데이터 조회하는 경우

* 와일드 카드 
  
  * %: 0개 이상 문자
  
  * _: 1개 단일 문자

### IS NULL / IS NOT NULL

* NULL 여부를 확인할 때 항상 = 대신 IS를 활용한다. 

### 부정연산자

* 같지 않다. (!=. ^=, <>)

* ~와 같지 않다. (NOT 칼럼명 =)

* ~보다 크지 않다. (NOT 칼럼명 >)

```sql
WHERE 칼럼명1 != 비교값1
    AND 칼럼명2 ^= 비교값2
    AND 칼럼명3 <> 비교값3
    AND NOT 칼럼명4 = 비교값4
    AND NOT 칼럼명5 > 비교값5;
```

### 우선순위

1. 괄호

2. NOT

3. 비교 연산자, SQL

4. AND

5. OR

#### 예문

```sql
--1.
WHERE HEIGHT = 175 OR HEIGHT = 183 AND WEIGHT = 80;
--2.
WHERE (HEIGHT = 175 OR HEIGHT = 183) AND WEIGHT = 80;
```

1. 키가 175이거나, 키가 183이면서 몸무게가 80인 사람

2. 키가 175 또는 183인 사람 중에서 몸무게가 80인 사람
   
   ↳ 괄호에 묶여있는 조건 먼저 인식하게 된다. 

## Aggregate Functions 집계 함수

* COUNT

* AVG

* MAX 

* MIN SUM

### COUNT

* 그룹의 항목 수를 센다.

* 조건에 만족하는 데이터 항목을 센다.

```sql
SELECT COUNT(*) FROM users;
```

↳ user 테이블의 레코드 총 개수를 조회한다. 

### AVG

* 값의 평균을 계산한다. 

```sql
SELECT AVG(컬럼) FROM 테이블이름;
```

```sql
SELECT AVG(age) FROM users WHERE age>=30;
```

↳ user 테이블에서 30살 이상인 사람들의 평균 나이를 조회한다. 

### MAX

* 그룹에 있는 최대값을 가져온다. 

```sql
SELECT MAX(컬럼) FROM 테이블이름;
```

```sql
SELECT first_name, MAX(balance) FROM users;
```

↳ user 테이블에서 계좌 잔액이 가장 높은 사람의 이름과 액수를 조회한다. 

### MIN

* 그룹에 있는 최소값을 가져온다. 

```sql
SELECT MIN(컬럼) FROM 테이블이름;
```

### SUM

* 값의 합을 계산한다. 

```sql
SELECT SUM(컬럼) FROM 테이블이름;
```

# 

# LIKE

* “query data based on pattern matching”

* 패턴 일치를 기반으로 데이터를 조회한다. 

* SQLite는 패턴 구성을 위해 2개의 wildcards를 제공한다. 
  
  * % percent sign
    
    * 0개 이상의 문자
    
    * '%' 자리에 문자열이 있을 수도 없을 수도 있다. 
  
  * _ underscore
    
    * 임의의 단일 문자
    
    * 반드시 '_' 자리에 한 개의 문자가 존재해야 한다. 

```sql
SELECT * FROM 테이블이름 WHERE 컬럼 LIKE '패턴';
```

* **2%**: 2로 시작하는 값

* **%2**: 2로 끝나는 값 

* **%2%**:  2가 들어가는 값

* **_2%**:  앞에 하나의 값이 들어가고 2, 두 번째가 2로 시작하는 값

* **1___**: 1로 시작하고 총 4자리인 값 (ex. 1000, 1001 등)

* **2_%_% / 2_ __%**: 2로 시작하고 적어도 3자리인 값 

```sql
SELECT * FROM users WHERE age LIKE '2_';
```

↳ user 테이블에서 나이가 20대인 사람만 조회한다. 

```sql
SELECT * FROM users WHERE first_name LIKE '%준';
```

↳ users 테이블에서 이름이 ‘준’으로 끝나는 사람만 조회한다. 

```sql
SELECT * FROM users WHERE phone LIKE '%-5114-%;
```

↳ users 테이블에서 중간 번호가 5114인 사람만 조회한다.

## ORDER BY

* "**sort** a result set of a query”

* 조회한 결과 집합을 정렬한다. 

* ASC: 오름차순 (default)

* DESC: 내림차순 

```sql
SELECT * FROM 테이블이름 ORDER BY 컬럼 ASC;
SELECT * FROM 테이블이름 ORDER BY 컬럼 DESC;
```

```sql
SELECT * FROM users ORDER BY age, last_name ASC LIMIT 10;
```

↳ users 테이블에서 나이 순, 성 순으로 **오름차순** 정렬하여 **상위 10개만** 조회한다.
