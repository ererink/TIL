# 객체

* 속성과 메서드를 가지고 있다.  
  
  * 속성은 값, 메서드는 함수를 실행시키는 것
  
  * **값과 함수**

* 클래스와 인스턴스 
  
  * 클래스가 사람이면, 인스턴스는 아이유, 유재석과 같은 의미이다.
  
  * **틀과 사례**

# ORM; Object-Relational-Mapping

* **객체 지향 프로그래밍 언어**를 사용하여 호환되지 않는 유형의 시스템 간의 데이터를 변환하는 프로그래밍 기술
  
  * SQLAIchemy, peewee, Dajango ORM 

* 파이썬으로 데이터베이스를 조작하는 것이다.
  
  * 객체로 DB를 조작한다."

```sql
Genre.objects.all()

==

SELECT * FROM Genre;
```

두 문장은 같은 의미를 가지고 있다. 

즉, 객체를 리스트로 담아서 보여주는 것이다. 

### 모델 설계 및 반영

<img title="" src="file:///C:/Users/yelki/OneDrive/바탕%20화면/TIL/SQL/SQL%20Summary.assets/orm_model.png" alt="orm_model.png" data-align="center" width="212">

#### 

#### 1. 클래스를 생성하여 원하는 DB의 구조를 만든다.

```python
class Genre(models.Model):
    name = models.CharField(max_length=30)
```

max_length=30는 varchar(30)와 같은 의미이다.

```python
from django.db import models

class Genre(models.Model):
```

Genre 클래스를 만들 때 models.Model 내부 클래스를 상속 받는다. 

내부 클래스를 상속받는 이유는 직접 클래스를 만드는 것이 아니라 미리 만들어진 기능들을 활용하고자 하는 것이다. 

```python
from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=30)
```

#### 2. 클래스의 내용으로 데이터베이스에 반영하기 위한 마이그레이션 파일을 생성한다.

```
python manage.py makemigrations
-> 마이그레이션 파일 생성

 python manage.py migrate
-> 마이그레이션은 DB에 반영된다.
```

### Migration

- Model에 생긴 변화를 DB에 반영하기 위한 방법이다.

- 마이그레이션 파일을 만들어 DB 스키마를 반영한다.

- 클래스를 바꾸면 알아서 수정해준다!

### Migration의 트랜잭션

```sql
BEGIN;

CREATE TABLE "db_genre" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "name" varchar(30) NOT NULL
);
COMMIT;
```

* BEGIN과 COMMIT의 기능

1000줄의 명령문을 작성하였다고 가정해보자.

1000줄의 명령문 모두 오류가 없다면 COMMIT을 하고, 1000줄 중 몇 줄에 오류났다면 ROLLBACK을 실행하여 되돌아가게 한다. 

오류가 없으면 모두 다 반영하여 명령문을 실행하고, 그 중 오류가 하나라도 있으면 반영하지 않는다. 

즉, BEGIN과 COMMIT 사이의 명령문들을 한 단위로 묶어서 실행하는 느낌으로 볼 수 있다. 

# ORM 기본 조작

## CREATE 생성

```python
# 1. create 활용
Genre.objects.create(name='발라드')

# 2. 인스턴스 조작
genre = Genre()
genre.name = '인디밴드'
genre.save()
```

```python
genres = Genre.object.all()

for genre in genres:
    print(genre.name)
```

for문을 통한 출력이 가능하다.

## 

## READ 조회

```python
# 1. 전체 데이터 조회
Genre.objects.all()
# <QuerySet [<Genre: Genre object (1)>, <Genre:Genre object (2)>]>  

# 2. 일부 데이터 조회(get)
Genre.objects.get(id=1)
# <Genre: Genre object (1)>   

# 3. 일부 데이터 조회(filter)
Genre.objects.filter(id=1)
# <QuerySet [<Genre: Genre object (1)>]>
```

### .get & .filter

#### .get(id=1)

* id가 1인 값을 가져온다. 
  
  * ('인디밴드')

* 반드시 **하나**여야 한다. 

* 없거나 많으면 오류를 띄운다.

* **PK**로 꺼낼 때 주로 사용한다. 



#### .filter(id=1)

* 결과가 무조건 **QuerySet**이다. 
  
  * (일종의 리스트)

* **PK 이외의 값**을 꺼낼 때 사용한다.

* .get과의 차이는 단일객체, 전체 쿼리셋과의 차이이다.
  
  * 즉, 리스트를 담고 안담고의 차이이다.





## UPDATE 수정

객체를 부른 후 수정한다. 

인디밴드를 인디음악으로 바꾸고자 한다. 

```python
# 1. genre 객체 활용
genre = Genre.objects.get(id=1)  

# 2. genre 객체 속성 변경
genre.name = '인디음악’  

# 3. genre 객체 저장
genre.save()
```

# 

## DELETE 삭제

객체를 부른 후 삭제한다. 

```python
# 1. genre 객체 활용
genre = Genre.objects.get(id=1)  

# 2. genre 객체 삭제
genre.delete()

Genre.object.get(id=1).delete()
# 한줄로 표현이 가능하다!
```

.delete()는 save 필요 없으며, 바로 반영된다.




