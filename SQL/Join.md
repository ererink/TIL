# Join

* 관계형 데이터베이스의 큰 장점이자 핵심적인 기능이다. 

* 일반적으로 데이터베이스에는 하나의 테이블에 많은 데이터를 저장하는 것이 아니라 여러 테이블로 나눠 저장한다. 
  
  * 그러므로 여러 테이블을 **결합**하여 출력하여 Join을 활용한다. 

* **기본키(PK)** 나 **외래키(FK)** 값의 관계에 의해 결합한다. 
  
  * 외래키는 다른 테이블의 기본키를 참조한 키이다. 

* 두 개의 테이블을 결과로 나타내고자 하는 것이다.

#### Join을 사용하는 이유

데이터를 수정할 때 용이하다. 

어느 한 커뮤니티의 질문 테이블에서  '홍길동'의 role을 수정한다고 가정해보자. 

![join](./SQL%20Summary.assets/join1.png)

'student'를 '학생'으로 수정하기 위해서 하나의 테이블에서 연속적으로 수정이 이뤄져야 한다. 즉, 해당되는 데이터를 일일이 다 바꿔줘야 한다. 만약 이 데이터가 4개가 아닌 400만개 이상이라면 수정이 어려운 상황이다. 

혹은 '홍길동'의 동명이인이 존재할 때 구별하지 못한다는 점이다. 

![join2](./SQL%20Summary.assets/join2.png)

위의 문제점을 해결하기 위해 유저의 별도 데이터베이스로 나눠서 관리할 수 있다. 

이때 질문 테이블의 고유한 값인 **id**를 사용하여 기본키 - 외래키를 통해 각 테이블을 연결시켜준다. 외래키를 통해 user 정보를 알 수 있는 것이다. 

### INNER JOIN

* 두 테이블에 일치하는 행만 반환한다.

* 조건에 일치하는 (동일한 값이 있는) 행만 반환한다. 

![inner join](./SQL%20Summary.assets/INNER%20JOIN.png)

![create table.png](./SQL%20Summary.assets/create%20table.png)

users, role, articles 테이블이 존재한다.

```sql
SELECT *
FROM users INNER JOIN role 
    ON users.id = role.id;


-- id  name  role_id  id  title
-- --  ----  -------  --  -----
-- 1   관리자   1        1   admin
-- 2   김철수   2        2   staff
-- 3   이영희   2        2   staff
```

↳ users 테이블의 id와 role 테이블의 id를 조인한다. 

![INNER JOIN 1.png](./SQL%20Summary.assets/INNER%20JOIN%201.png)

```sql
SELECT *
FROM users JOIN role 
    ON users.id = role.id
WHERE role.id = 2;

-- id  name  role_id  id  title
-- --  ----  -------  --  -----
-- 2   김철수   2        2   staff
-- 3   이영희   2        2   staff
```

↳ 스태프만 출력한다. 

![INNER JOIN 2.png](./SQL%20Summary.assets/INNER%20JOIN%202.png)

```sql
SELECT *
FROM users JOIN role 
    ON users.id = role.id
ORDER BY users.name DESC;

-- id  name  role_id  id  title
-- --  ----  -------  --  -----
-- 3   이영희   2        2   staff
-- 2   김철수   2        2   staff
-- 1   관리자   1        1   admin
```

↳ 이름을 내림차순으로 출력한다. 

* Join의 횟수를 센다면 join할 테이블에서 1을 뺀다.

    (2개 테이블 조인 시 조인은 1개 사용, 3개 테이블 조인 시 조인 2개 사용)

### 

### OUTER JOIN

```sql
SELECT *
FROM 테이블1 [LEFT|RIGHT|FULL] OUTER JOIN 테이블2            
     ON 테이블1.칼럼 = 테이블2.칼럼;
```

* 동일한 값이 없는 행도 반환한다. 

* LEFT/RIGHT/FULL을 지정한다. 

![outer join](./SQL%20Summary.assets/OUTER%20JOIN.png)
#### LEFT OUTER JOIN

```sql
SELECT *
FROM articles LEFT OUTER JOIN users
    ON articles.users_id = users.id;
```

↳ users 테이블의 id와 role 테이블의 id를 left join한다.

![left join](./SQL%20Summary.assets/left%20join.png)

article 테이블을 기준으로 user 테이블이 join 되었다. 

```sql
SELECT *
FROM articles LEFT OUTER JOIN users
    ON articles.users_id = users.id
WHERE articles.users_id IS NOT NULL;
```

↳ LEFT OUTER JOIN 시 NULL 값을 빼고 출력한다. 

![left join2](./SQL%20Summary.assets/join2.png)

#### FULL OUTER JOIN

```sql
SELECT *
FROM articles FULL OUTER JOIN users
    ON articles.user_id = users.id;
```

↳ 모든 게시글과 모든 사용자 정보를 출력한다. 

![left join](./SQL%20Summary.assets/left%20join.png)

LEFT OUTER JOIN은 왼쪽 테이블(articles.users_id)에 상응하는 오른쪽 테이블(users.id)을 붙이는 것이지만, 

FULL OUTER JOIN은 왼쪽 테이블(articles.users_id)에 상응하는  오른쪽 테이블(users.id)을 붙이고, 오른쪽에 상응하는 왼쪽 테이블 붙이는 것이다. 

### CROSS JOIN

* 모든 데이터를 조합한다. 

```sql
SELECT *
FROM users CROSS JOIN role;

-- id  name  role_id  id  title
-- --  ----  -------  --  -------
-- 1   관리자   1        1   admin
-- 1   관리자   1        2   staff
-- 1   관리자   1        3   student
-- 2   김철수   2        1   admin
-- 2   김철수   2        2   staff
-- 2   김철수   2        3   student
-- 3   이영희   2        1   admin
-- 3   이영희   2        2   staff
-- 3   이영희   2        3   student
```

↳ 가능한 모든 조합을 다 출력한다. 

#### 3개의 테이블 조인

```sql
SELECT *
FROM articles
    JOIN users
        ON articles.user_id = users.id
    JOIN role
        ON users.role_id = role.id;

-- id  title  content  user_id  id  name  role_id  id  title
-- --  -----  -------  -------  --  ----  -------  --  -----
-- 1   1번글    111      1        1   관리자   1        1   admin
-- 2   2번글    222      2        2   김철수   2        2   staff
-- 3   3번글    333      1        1   관리자   1        1   admin
```
