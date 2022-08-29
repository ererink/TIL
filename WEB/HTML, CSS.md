# HTML; Hyper Text Markup Language

웹 페이지(문서)의 구조를 나타낸다.

## HTML 스타일 가이드

```html
<body>
    <h1> HTML </h1>
    <ul>
        <li> hi </li>
        <li> bye </li>
    </ul>
</body>
```

2 space 스타일 가이드이다.

# HTML 기본 구조

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Document</title>
</head>
<body>

</body>
</html>
```

## html

* 문서의 최상위(root) 요소

## head

* 문서 메타 데이터 요소가 들어간다. 
  
  * 문서 제목, 인코딩, 스타일, 외부 파일 로딩 등

* 정보의 정보 

* 만들고자하는 문서를 위한 데이터이다. 
  
  * < title>: 브라우저 상단 타이틀 
  
  * < meta> 
  
  * < link>: 외부 리소스 연결 (CSS 파일 등)
  
  * < script>:  JS스크립트
  
  * < style>: CSS 작성

```html
<head>
  <title>HEAD EXAMPLE</title>
  <meta charset="UTF-8">
  <link href="style.css" rel="stylesheet">
  <script src="javascript.js"></script>
  <style>
    p {
       color: black;
    }
  </style>
</head>
```

## body

* 문서 본문 요소가 들어간다. 

## 요소 Element

<img title="" src="file:///C:/Users/yelki/OneDrive/바탕%20화면/TIL/WEB/WEB.assets/element.png" alt="element.png" data-align="left">

요소에는 여는 태그와 닫는 태그로 구성되어있다. 

* 요소는 태그를 통해 해당 내용을 감싸며 해당 정보의 성격과 의미를 정의한다. 

* 닫는 태그가 없는 태그들
  
  * br: 띄어쓰기
  
  * hr: 수평선
  
  * img:이미지
  
  * input
  
  * link
  
  * meta

* 요소는 중첩될 수 있다. 

```html
<html>
    <head>
    </head>

    <body>
    </body>
```

중첩되는 것은 태그로 표현한다.

## 속성 Attribute

![arrtibute.png](C:\Users\yelki\OneDrive\바탕%20화면\TIL\WEB\WEB.assets\arrtibute.png)

* 태그별로 사용할 수 있는 속성은 다르다. 

* 속성에 해당하는 속성값을 ""안에 넣는다. 

* 공백없이 작성해야 한다. 

* 태그의 부가적인 정보를 설정한다. 
  
  * 경로나 크기와 같은 추가적인 정보를 제공한다.

* 이름과 값이 하나의 쌍으로 존재한다. 

* 글로벌 속성을 가진다. (HTML Global Attribute)
  
  * 태그와 상관없이 사용 가능한 속성이다.
  
  * id
  
  * class
  
  * style

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Document</title>
</head>
<body>
  <!-- 주석 -->
  <h1>title</h1>
  <p>body</p>
  <span>inline element</span>
  <a href="https://www.google.com">구글 링크 첨부</a>
</body>
</html>
```

## 렌더링

* 웹을 만든 코드를 사용자가 볼 수 있도록 웹 사이트로 바꾸는 과정이다.

* 변환 과정을 뜻한다. 

* 화면을 만드는 것이다.

## DOM 트리, Document Object Model

* 텍스트 파일인 HTML 문서를 브라우저에서 렌더링 하기 위한 구조이다. 

* HTML 문서에 대한 모델을 구성한다.

* 계층구조를 가지고 있다. 

* 자바스크립트를 통해 DOM을 조작한다. 

* 부모-자식 관계, 형제관계를 표현한다. 

![dom.png](C:\Users\yelki\OneDrive\바탕%20화면\TIL\WEB\WEB.assets\dom.png)

(image from wikipedia)

## 텍스트 요소

* <a href></a>: 링크

* <b></b>: 굵은 글씨

* < strong></strong>: 강조

* < i></i>: 이탤릭

* < em></em>: 이탤릭 강조

* < br>: 개행

* < img>: 이미지

* < span></span>: 의미없는 인라인 컨테이너

### 그룹 컨텐츠

* < p></p>: 문단

* < hr>: 수평선

* < ol></ol>: 순서 있는 리스트

* < ul></ul>: 순서 없는 리스트

* < pre></pre>: 작성한 내용 그래도 표현

* < blockquote></blockquote>: 인용문, 들여쓰기로 표현

* < div></div>: 의미 없는 블록 레벨 컨테이너

### heading

* 제목을 위한 것이며, 글씨를 키우기 위해서 사용해선 안된다.

* < h1>

* < h2>

* < h6>

# CSS; Cascading Style Sheets

* 스타일을 지정하기 위한 언어이다.

![css.png](C:\Users\yelki\OneDrive\바탕%20화면\TIL\WEB\WEB.assets\css.png)

### CSS 구문

```css
<style>
    h1 {
        color: blue;
        font-size: 15px;
    }
</style>
```

## CSS 정의 - 인라인

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1 style="color: blue; font-size: 100px;">Hello</h1>
</body>
</html>
```

body 구문의 태그에 style 속성을 활용한다.

## CSS 정의 - 내부참조

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    h1 {
       color: blue;
       font-size: 100px;
    }
</style>
</head>
<body>
</body>
</html>
```

## CSS 정의 - 외부참조

* css 파일을 만들어 해당 파일에 style을 지정한다.

* 외부 css 파일을 html 파일의 <head> 내 <link>를 통해 불러온다.

### 내부참조 및 외부참조를 사용하는 이유

* 유지보수, 재사용 가능성을 늘리기 위해 내부참조를 사용한다. 

* 인라인(태그선택자)을 사용하게 된다면, 
  
  * 수정 시 모든 태그가 다 수정되기 때문에 클래스를 이용한다. 

```css
.title-brown {
    color: brown;
}

<h2 class="title-brown">내용</h3>
```

↳ 우선순위: id > class > tag

태그보다 클래스의 순위가 더 높기 때문에 아무리 태그로 스타일을 선택해도 클래스가 있는 한 적용되지 않는다.

```css
.title-brown {
    color: brown;
}
.title-blue{
    color: blue;
}

<h2 class="title-blue title-brown">내용</h3>
```

blue 클래스 선언이 더 늦게 되었기 때문에 title-blue가 적용된다. 

```css
.title-brown {
    color: brown;
}
.title-blue{
    color: blue;
}

<h2 id="title-blue" class="title-brown">내용</h3>
```

id로 선언하면 class가 적용되지 않는다. 

다만, 일반적으로 css 스타일링은 **클래스**를 주로 사용한다. 

id는 주로 JS로 개발할 때 활용한다. id는 단일 id로 사용하는 것을 권장한다. (1번만 사용!)
