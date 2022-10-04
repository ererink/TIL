# 1. 환경설정
## 1. 가상환경 생성 및 실행
```bash
$ python -m venv recap-venv
$ source recap-venv/Scripts/activate
```
## 2. Django 설치
```bash
$ pip install django==3.2.13
$ pip install black
$ pip list
Package         Version
--------------- -------
asgiref         3.5.2
black           22.8.0
click           8.1.3
colorama        0.4.5
Django          3.2.13
mypy-extensions 0.4.3
pathspec        0.10.1
pip             22.0.4
platformdirs    2.5.2
pytz            2022.4
setuptools      58.1.0
sqlparse        0.4.3
tomli           2.0.1

$ pip freeze > requirements.txt
```

## 3. Django 프로젝트 및 앱 생성
```bash
$ django-admin startproject pjt .
$ django-admin startapp appp
```

# 2. 세부설정

## 1. project의 urls 설정
```django
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("appp.urls")),
]
```
생성한 project에 urls.py에서 app의 urls.py와 연결해준다.

```django
from django.urls import path
from . import views
app_name = "appp"

urlpatterns = [
    path("", views.index, name="index"),
]
```
appp 폴더 안에 urls.py을 생성한다. 

## 1-2. settings.py에서 앱 이름 추가
프로젝트 폴더 안 settings.py에서 'INSTALLED_APPS'에 앱 이름을 추가한다.

## 2. views 함수 생성
```django
def index(request):
    
    return render(request)

```
동작할 기능을 함수로 선언한다. 

## 3. templates 폴더 생성 및 appp 폴더 생성
.html을 생성해주기 위해 appp 폴더 안에 templates 폴더를 생성한다. 
tempaltes 폴더 안에 앱 이름과 동일한 이름인 appp 폴더를 생성한다. .html들은 해당 폴더 안에 존재하도록 한다. 

## 4. base.html 생성
프로젝트와 앱 폴더와 동일하게 제일 상단에서 templates 폴더를 생성한다. 이후 base.html을 해당 폴더에 넣어준다. 
모든 html 파일은 base.html의 양식을 인식하게 된다. 
base.html에 홈페이지 이름과 bootstrap url을 넣어준다. 

```django
        "DIRS": [BASE_DIR / "templates"],

```
settings.py에서 'TEMPLATES'에 DIRS의 값을 변경해준다. 

## 5. models.py 데이터베이스 스키마 생성
데이터베이스에 넣어줄 데이터의 양식을 만들어준다. 


# 3. CRUD 기능 구현
## 1. 대문 생성 (index.html)
게시판의 첫 화면을 index.html에 구현한다.
데이터베이스에 저장된 글 제목/내용/작성시간/수정시간을 보여준다. 이를 위해서 for문을 사용하여 저장된 데이터를 보여준다. 

글을 수정할 수 있도록 버튼(a태그)을 만든다. 이를 위해서 버튼에 수정 페이지로 넘어갈 수 있도록 한다. 

## 2. create
데이터를 DB에 저장하는 기능이다. 
여기서 method 종류 중 post는 데이터를 보내는 것이고, get은 조회하는 것이다. 

유효성 검사(is_valid())를 통해 데이터 형식이 유효하다면 DB에 데이터를 저장한다. (appp_form.save())

## 3. update
특정 id(pk)값을 가져온 후 새로운 데이터를 instance로 넘겨준다. 

## 4. detail
특정 id(pk)값을 가져온 후 해당 페이지에서 title, content 등 해당 id의 데이터를 보여준다. 