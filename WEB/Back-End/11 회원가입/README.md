# 회원가입
![회원가입](./movie.assets/%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85.gif)

# 회원목록
![회원목록](./movie.assets/%ED%9A%8C%EC%9B%90%EB%AA%A9%EB%A1%9D.gif)
## 목표

Django **Auth**를 활용한 회원가입이 가능한 서비스를 개발합니다.

## 요구사항

### 모델 Model

- 모델 이름 : User
    
    Django **AbstractUser** 모델 상속
    

### **폼 Form**

- Django 내장 회원가입 폼 UserCreationForm을 상속받은 CustomUserCreationForm 생성 후 활용
    
    해당 폼은 아래 필드만 출력합니다.
    
    - username
    - email
    - password1
    - password2

### 기능 View

회원가입 Create

- `POST` http://127.0.0.1:8000/accounts/signup/
- CustomUserCreationForm을 활용해서 회원가입 구현

회원 목록 조회 Read(index)

- `GET` http://127.0.0.1:8000/accounts/

회원 정보 조회 Read(detail)

- `GET` http://127.0.0.1:8000/accounts/<user_pk>/

### 화면 Template

메인페이지

- `GET` http://127.0.0.1:8000/
- 회원가입 페이지 이동 버튼
- 회원 목록 페이지 이동 버튼
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/fb2edac6-5056-4b5d-a067-200417f8149d/Untitled.png)
    

회원가입 페이지

- `GET` http://127.0.0.1:8000/accounts/signup/
- 회원가입 폼 ****
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e0faec52-56a9-4a13-8b3f-68d40622a98f/Untitled.png)
    

회원 목록 페이지

- `GET` http://127.0.0.1:8000/accounts/
- 회원 목록 테이블
- **username** 클릭 시 해당 회원 조회 페이지(프로필 페이지)로 이동
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9b3e71b7-966b-4982-a51c-d537d9a927d0/Untitled.png)
    

회원 조회 페이지(프로필 페이지)

- `GET` http://127.0.0.1:8000/accounts/<user_pk>/
- 회원 정보 출력

# 회원가입 기능

## 1. accounts App 만들기

## 2. setting.py 입력
1. 앱 등록
2. `AUTH_USER_MODEL = 'auth.User'` 입력

## 3. models.py 입력
```python
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
```

## 4. admin.py 입력
```python
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)
```

## 5. makemigrations, migrate 진행
auth_user 테이블이 아니라 accounts_user 테이블을 사용하게 됨

