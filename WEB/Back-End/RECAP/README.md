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
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("appp.urls")),
]
```
생성한 project에 urls.py에서 app의 urls.py와 연결해준다.

```python
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
```python
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

```python
"DIRS": [BASE_DIR / "templates"],
```
settings.py에서 'TEMPLATES'에 DIRS의 값을 변경해준다. 

## 5. models.py 데이터베이스 스키마 생성
데이터베이스에 넣어줄 데이터의 양식을 만들어준다. 

## 6. migration 생성



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


# Django 개념 정리
1. url로 요청을 받아서
2. 처리하고
3. 응답을 한다. 

틀에 박힌 일이다 ==> Framework
http 서버 클라이언트 모델을 가지고 있기 때문에

DB에서 값을 가져오고 저장하는 로직이다. 
이를 도와주고 있는 것이 Django ORM.

처리하고 응답하는 것은 views.py가 담당하고 있다. 
HTML을 만드는 것은 templates이 담당하고 있다. 

이것이 MTV 패턴이다!


결국 궁극적인 목표는 서비스 기능을 만들기 위해 코드를 작성하는 것이다. 
서비스 기능 중 게시판 기능의 CRUD를 만들고 있는 것이다. 


## <게시판>
* 생성
* 조회 
* 삭제 
* 수정

1. URL을 정의한다. 
생성: 사용자에게 HTML Form을 제공, DB 저장 과정이 필요하다. 
URL:/articles/new
URL:/articles/create
views: new, create

조회: 글을 누르면 DB의 값을 조회하도록 한다. 
URL:/articles/pk
views: detail

삭제: 버튼을 누르면 DB의 값을 삭제한다. 
URL:/articles/pk/delete
views: delete

수정: HTML Form으로 주되 기존 값과 같이 준다, DB 저장 과정이 필요하다. 
URL:/articles/pk/edit
URL:/articles/pk/update
views: edit, update


URL로 요청을 받는데, HTTP 요청 메세지로서 표현이 가능하다.
HTTP 요청 메서드 4가지: Path / 메서드 / 헤더 / 프로토콜

variable routing: 요청하는 url에서 값을 받아 오는 것이다. pk를 사용해서 특정 값을 가져온다. 




## ModelForm 
생성과 수정에서 DB에 저장하는 과정을 도와준다. 

### 왜 ModelForm을 사용하는가?
1. DB 필드가 HTML Form과 매우 밀접한 관계를 가지고 있다. 
2. 사용자로부터 받은 input값을 DB에 들어가기 전에 유효성 검사가 필요하다. 유효성 검사를 같이 처리하기 때문에
ModelForm을 설계한 것이다. 

### 역할
1. 선언된 모델에 따른 필드를 구성한다. 
2. 유효성 검사를 진행한다. 

```python
from django import forms
from .models import Recap

class RecapForm(forms.ModelForm):
    class Meta:
        model = Recap
        fields = ["title", "content"]
```
(model = Recap)어떠한 DB의 (fields = )어떠한 필드인지 정하는 것이다. 

```python
appp_form = RecapForm(request.POST)
        if appp_form.is_valid():
            appp_form.save()
            return redirect("appp:index")
```
유효성 검사를 한다. 
유효성 검사를 통과하였으면 DB에 저장할 수 있고, 
통과하지 못하였으면 에러 메세지를 띄운다. 


![유효성검사로직](./recap.assets/%EC%9C%A0%ED%9A%A8%EC%84%B1%20%EA%B2%80%EC%82%AC%20%EB%A1%9C%EC%A7%81.png)


#### 응답
1. 생성(create): crate.html을 준다.
2. 생성(new): redirect로 상세 페이지를 준다. 
3. 조회(detail): detail.html의 context를 담아서 준다. 
4. 삭제 시 redirect로 목록 페이지(혹은 index를 보여준다)
5. update.html을 제공한다.
6. redirect로 상세 페이지를 준다. 


# 코드 정리
### 가상환경을 쓰는 이유
프로젝트별 별도 패키지를 관리하기 위해서

Django의 주요 기능 단위인 APP 별로 MTV 구조를 갖게 된다. + urls.py를 통해 별로도 url을 관리한다. 

### urls.py
App 단위의 URL을 관리하기 위함이다. 
경로들이 쭉 나열되어 있는 것이다. 
어떠한 views.py를 가르키고 있는지 나열한 것이다. 


```python
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("appp.urls")),
]
```

"appp.urls"은 모듈을 뜻하는 것이다. 즉, articles의 urls.py를 의미하는 것이다. 

활용: `articles:index` => `/articles` 와 같은 의미이다. 
* template에서의 활용
```python
```

* views에서의 활용
```python
```



### views.py

```python
def create(request):
    posts = Recap.objects.order_by("-pk")

    context = {
        "posts": posts,
    }
    return render(request, "appp/create.html", context)
```

* HTML Form 태그 활용시 핵심
    * 어떤 필드를 구성할 것인지(name, value)
    * 어디로 보낼 것인지(action, method)

```html
<form action="{% url 'appp:create' %}" method="POST">
    {% csrf_token %}
    {{ appp_form.as_p }}
    <input type="submit" value="글쓰기">
</form>
```

### GET & POST
GET == 제공 및 조회
POST == 데이터 처리 및 저장, 보내기 

글 제목에 123과 글 내용에 123을 적었을 때

* GET
url: /articles/create/?title=123&content=123
views.py: request.GET

* POST
url: /articles/create
views.py: request.POST

html파일에서 input 태그에 `name='~'` 으로 연결해둔 것이 
request.GET 혹은 request.POST로 보내주는 것이다. 
(title:'123', content:'123' 로 넘겨준다.)

#### request 객체
요청과 응답을 처리하는 객체이다. 
페이지에 요청이 들어오면 HTTP request 객체를 만든다. 
view function에 첫번째 인자로 넘겨준다. 
