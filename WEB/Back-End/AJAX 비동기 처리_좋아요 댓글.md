# AJAX, Axios

## 비동기란?

요청을 보낸 후 응답을 기다리지 않고 다음 동작(코드)이 이루어지도록 하는 것이다. 

즉, 응답이 돌아올 동안 다음 코드와 동작을 처리하여 실행하게 된다. 



## Axios

AJAX 요청이 도착하면 성공 및 실패 여부를 따지고 약속한 코드를 실행하도록 해준다. 

```html
<script src="..."></script>
<script>
    const URL = '...'
    axios.get(URL)
        .then(response => console.log(response.data))
        .catch(err => console.log('${err}!!!')
    console.log('Hii')
</script>
```

성공 시 .then 코드를 실행하고, 실패 시 .catch 코드를 실행한다. 



## Axios를 사용하는 이유

브라우저를 히애하면 쉽다. 

자바스크립트가 비동기적이 아닌 동기적이라면 브라우저가 멈춰있는 상황을 많이 겪을 것이다. 

비동기적이기 때문에 화면이 띄워질 동안 기다리지 않아도 되는 것이다. 이는 사용자 경험을 위한 것이기도 하다.

서버 측면에서 생각해보자면, 리소스를 적게 쓸 수 있다. HTML을 새롭게 개선해서 응답하는 것이 아닌 클라이언트 측에서 조작하는 행위이기 때문이다.



'구글맵'이 대표적인 비동기 처리의 예이다. 

지도를 옮겨가면서 볼 때 계속해서 새로고침하여 지도를 보여주는 것이 나닌 연속적으로 지도를 보여주는 것이다. (연속적으로 데이터를 보내주는 것이다. )



## 과정

1. 버튼을 눌러 비동기로 요청을 하고
2. 응답을 JSON으로 준다.

버튼을 클릭하면 함수를 실행해준다. 

axios는 url로 요청을 보내준다. 이 요청은 요청을 보내서 처리가 완료되면 실행 시켜주겠다는 '약속'을 가지고 있다. (성공 - then, 실패 - catch)

성공해서 받은 응답 객체를(장고 객체 X) 활용하여 조작하는 것이다. (Javascript로 실행)



# 좋아요 기능 비동기 적용하기

## 1. detail.html 작성

```html
{% if request.user.is_authenticated %}
  {% if request.user in article.like_users.all %}
    <i id="like-btn" data-article-id="{{ article.pk }}" class="bi bi-heart-fill"></i>
    <i id="like-btn" data-article-id="{{ article.pk }}" class="bi bi-heart"></i>
  {% endif %}
<span id="like-count">{{ article.like_users.count }}</span>

```

좋아요의 하트 이모티콘에 id를 설정해준다. 



```html

<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
<script>
  const likeBtn = document.querySelector('#like-btn')
  likeBtn.addEventListener('click', function (event) {
    console.log(event.target.dataset)
    axios({
      method: 'get',
      url: `/articles/${event.target.dataset.articleId}/like/`
    })
    .then(response => {
      console.log(response)
      console.log(response.data)
   
      if (response.data.isLiked === true) {
        event.target.classList.add('bi-heart-fill')
        event.target.classList.remove('bi-heart')
      } else {
        event.target.classList.add('bi-heart')
        event.target.classList.remove('bi-heart-fill')
      }
      const likeCount = document.querySelector('#like-count')
      likeCount.innerText = response.data.likeCount
    })
  })
</script>
```

자바스크립트를 `script` 태그로 작성해준다. 

`const likeBtn = document.querySelector('#like-btn')`: 좋아요 버튼을 선택한다.

`  likeBtn.addEventListener('click', function (event) {`: addEventListener로 좋아요 버튼을 클릭하면 함수를 실행하도록 한다. 

`axios({...}) .then(...)`이후 서버로 비동기 요청을 한다. 

`if (response.data.isLiked === true) {`: Boolean을 넣어줘서 좋아요를 누르고 취소하는 것에 빈하트/채운 하트를 구별하여 화면에 띄울 수 있도록 한다. 



## 2. views.py 작성

```python
from django.http import JsonResponse

def like(request, pk):
	...
  if request.user in article.like_users.all(): 
	   ...
     is_liked = False

  else:
    ...
    is_liked = True
    context = {'isLiked': is_liked, 'likeCount': article.like_users.count()}
    return JsonResponse(context)
```

`JsonResponse` 를 불러온다.

if문을 통해 True/False값을 `is_liked`에 할당한다. 





# 댓글 기능 비동기 적용하기

## 1. detail.html

```html
{% if request.user.is_authenticated %}
<form id="comment-form" data-article-id="{{ article.pk }}">
	  {% csrf_token %}
		...
</form>
```

댓글을 생성하는 form 태그에 id를 설정한다. 



```html
<div id="comments">
  {% for comment in comments %}
    <p> {{ comment.user.username }} | {{ comment.content }}</p>
	...
</div>
```

댓글 목록을 띄워주는 div 태그에도 id를 설정한다. 



```html
<script>
  // 댓글 생성 Form
  const commentForm = document.querySelector('#comment-form')
  const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
  commentForm.addEventListener('submit', function(event) {
    event.preventDefault();
    axios({
      method: 'post',
      url: `/articles/${event.target.dataset.articleId}/comments/`,
      headers: {'X-CSRFToken': csrftoken},
      data: new FormData(commentForm) // 폼에 있는 정보를 data로 넘겨줄 수 있도록 변환
    })
    .then(response => {
      console.log(response.data)
      // 댓글을 추가하는 로직, 댓글 정보를 넘겨준다.
      const comments = document.querySelector('#comments')
      const p = document.createElement('p')
      p.innerText = `${response.data.userName} | ${response.data.content}`
      const hr = document.createElement('hr')
      comments.append(p, hr) 
      commentForm.reset()
    })
  })
</script> 
```

`  const csrftoken = document.querySelector(...`: querySelector로 상단의 id로 설정한 commentForm을 가져온다. 

POST요청 시 CSRF token로 인해 오류가 뜨기 때문에 CSRF token을 AJEX로 보내는 역할을 한다.

` data: new FormData(commentForm)`: axios 구문에 데이터를 넘겨준다.

` const comments = document.querySelector('#comments')`: querySelector로 상단의 id로 설정한 comments를 가져온다. 이는 댓글 정보를 가져오기 위함이다. 

` const p = document.createElement('p')`, 

` p.innerText = ${response.data.userName} | ${response.data.content}`: p태그와 함께 HTML 요소를 만들어 반환해준다. username과 댓글을 반환해주는 것이다.

`comments.append(p, hr) `: 상단에 생성 및 반환한 댓글 정보를 comments에 넣어준다.



----------------

JSON은 문자열로 변환한다.

문자열로 해석해서 전달해주면 파이썬은 객체에 맞춰서 해석한다. 

파이썬은 리스트 안에 딕셔너리로 인식하고, 자바스크립트는 배열 안에 객체로 인식한다.

이러한 과정을 Parsing이라고 한다. 

즉, 파이썬의 딕셔너리와 자바스크립트의 객체를 JSON으로 Parsing하면 JSON으로 인해 문자열로 변환하는 것이다. 

