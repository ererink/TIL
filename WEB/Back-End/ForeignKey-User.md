# ForeignKey - User 정보 가져오기



## 1 : N (User - Comment)

User 모델과 Comment 모델 간의 관계를 설정한다. 

0개 이상의 댓글은 1개의 회원에 의해 작성될 수 있다. 



## 목표

accounts 앱 (articles와는 다른 앱)에서 User 정보를 가져와,

* 게시물과 댓글에 username을 함께 보여준다.

* 인증된 회원의 댓글을 작성할 수 있도록 한다. 

* 작성 전 로그인이 될 수 있도록 구현한다.  



# 구현

## 1. User 모델을 참조하는 외래키 작성

```python
# articles/models.py

class Article(models.Model):
    ...
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Comment(models.Model):            
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ...
```

Comment 모델에 User 모델을 참조하는 외래키를 작성한다. 



## 1-1. makemigrations, migrate

NOT NULL 제약조건이 있기 때문에 user_id가 생성되지 않는다. 

기본값을 설정할 수 있는 메세지를 잘 보고 입력한다!



## 2. views.py 작성

```python
# articles/views.py

def comments_create(request, pk):
     article = Article.objects.get(pk=pk)
     comment_form = CommentForm(request.POST)

     if comment_form.is_valid():
         comment = comment_form.save(commit=False)
         comment.article = article
         comment.user = request.user
         comment.save()
     return redirect('articles:detail', article.pk)
```

`comment.user = request.user` : 댓글 작성 시 작성자 정보가 함께 저장될 수 있도록 요청받은 user를 comment(댓글 form을 받은 변수)에 할당한다. 



## 3. 게시글 및 댓글 작성자 출력

## 3. detail.html, index.html 작성

```python
<!-- articles/detail.html -->

<h1 class='fw-bold'>{{ article.title }}</h1>
    ...
    <h3>{{ article.user.username }}</h3>
    <p>{{ article.content }} </p>
```

`{{ article.user.username }}` : 게시글의 작성자를 출력한다. 



```python
{% for comment in comments %}
  <li>
    {{ comment.user }} - {{ comment.content }}
    <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST">
     {% csrf_token %}
     <input type="submit" value="DELETE">
    </form>

```

`{{ comment.user }}`: 댓글의 작성자를 출력한다. 





## 댓글 삭제 시 작성자 확인

삭제를 요청하는 사람과 댓글을 작성한 사람을 비교하여 **본인의 댓글**만 삭제 할 수 있도록 한다. 



## 1. views.py 작성

```python
# articles/views.py
def comments_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)

    if request.user == comment.user:
        comment.delete()
    return redirect('articles:detail', article_pk)
```

`if request.user == comment.user:` : 요청한 유저와 댓글을 작성한 유저가 일치하는지 확인해준다.



## 2. detail.html 작성

```python
{% for comment in comments %}
   <li>
     {{ comment.user }} - {{ comment.content }}
     {% if request.user == comment.user %}
        <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST">
         {% csrf_token %}
         <input type="submit" value="DELETE">
        </form>
      {% endif %}
...
```

`{% if request.user == comment.user %}`: 요청한 유저와 댓글을 작성한 유저가 일치하는지 확인해준다.
