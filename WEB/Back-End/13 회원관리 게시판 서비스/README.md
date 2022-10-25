# 회원정보 수정하기
![회원정보 수정](./accounts.assets/%ED%9A%8C%EC%9B%90%EC%A0%95%EB%B3%B4%20%EC%88%98%EC%A0%95.gif)

# 회원가입
![회원가입](./accounts.assets/%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85.gif)

# 로그인 및 로그아웃
![로그인](./accounts.assets/%EB%A1%9C%EA%B7%B8%EC%9D%B8.gif)<br>
네비게이션 바의 이름을 누르면 회원정보 페이지로 넘어갑니다.

# 회원 목록
![회원목록](./accounts.assets/%ED%9A%8C%EC%9B%90%EB%AA%A9%EB%A1%9D.gif)<br>
회원 이름을 누르면 회원정보 페이지로 넘어갑니다. 


## 목표

Django Auth를 활용한 회원 관리가 가능한 게시판 서비스를 개발합니다.

## 요구사항

### 모델 Model

- 모델 이름 : User
    
    Django **AbstractUser** 모델 상속
    

### **폼 Form**

회원가입

- Django 내장 회원가입 폼 UserCreationForm을 상속 받아서 **CustomUserCreationForm** 작성&활용
    
    해당 폼은 아래 필드만 출력합니다.
    
    - username
    - password1
    - password2

로그인

- Django 내장 로그인 폼 **AuthenticationForm 활용**

회원 정보 수정

- Django 내장 폼 UserChangeForm을 상속 받아서 **CustomUserChangeForm** 작성&활용
    
    해당 폼은 아래 필드만 출력합니다.
    
    - first_name
    - last_name
    - email

### 기능 View

회원가입

- `POST` http://127.0.0.1:8000/accounts/signup/
- CustomUserCreationForm을 활용해서 회원가입 구현

회원 목록 조회

- `GET` http://127.0.0.1:8000/accounts/

회원 정보 조회

- `GET` http://127.0.0.1:8000/accounts/<user_pk>/

로그인

- `POST` http://127.0.0.1:8000/accounts/login/
- **AuthenticationForm**를 활용해서 로그인 구현

로그아웃

- `POST` http://127.0.0.1:8000/accounts/logout/

회원 정보 수정

- `POST` http://127.0.0.1:8000/accounts/<user_pk>/update/
- **CustomUserChangeForm**를 활용해서 회원 정보 수정 구현

### 화면 Template

네비게이션바, Bootstrap <nav>

- 로그인 상태에 따라 다른 화면 출력
    1. 로그인 상태
        - 로그인 한 사용자의 Username 출력
            - Username을 클릭하면 회원 조회 페이지로 이동
        - 로그아웃 버튼
    2. 비 로그인 상태
        - 로그인 페이지 이동 버튼
        - 회원가입 페이지 이동 버튼
    

로그인 페이지

- `GET` http://127.0.0.1:8000/accounts/login/
- 로그인 폼
- 회원가입 페이지 이동 버튼

회원가입 페이지

- `GET` http://127.0.0.1:8000/accounts/signup/
- 회원가입 폼

회원 목록 페이지

- `GET` http://127.0.0.1:8000/accounts/
- 회원 목록 출력
- 회원 아이디를 클릭하면 해당 회원 조회 페이지로 이동

회원 조회 페이지(프로필 페이지)

- `GET` http://127.0.0.1:8000/accounts/<user_pk>/

회원 정보 수정 페이지

- `GET` http://127.0.0.1:8000/accounts/<user_pk>/update/