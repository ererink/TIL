# Javascript

* 브라우저 화면을 동적으로 만들어준다. 

* 브라우저를 조작할 수 있는 유일한 언어이다. 

* 동적 언어이다. 
  
  * 웹 페이지나 앱의 서로 다른 화면을 보여줄 수 있고 새로운 콘텐츠를 생성할 수 있다. 



```js
<script>

  // JavaScript goes here

</script>

```

script 요소를 사용한다. 





# 브라우저에서의 작업

## DOM, Document Object Model

* HTML, XML과 같은 문서를 다루기 위한 문서 프로그래밍 인터페이스이다. 

* HTML 콘텐츠를 추가/제거/변경하고, 동적으로 페이지에 스타일을 추가할 수 있다. 
  
  * DOM API를 사용한다. 

* 문서를 구조화한다.
  
  * 각 요소는 **객체**(object)로 취급한다.
    
    * 하나의 객체로 취급하여 다루는 **논리적 트리 모델**

* 속성 접근, 메서드 활용뿐만 아니라 프로그래밍 언어적 특성을 활용한 조작 가능

* 주요 객체
  
  * window: 최상위 객체
  
  * document: 페이지 컨텐츠의 Entry Point 역할
  
  * navigator, location, history, screen



#### 파싱 (Parsing)

* 구문 분석 및 해석

* DOM Tree로 만드는 과정이다.



#### DOM 조작

1. 선택

2. 변경

Document는 문서 한 장(HTML)에 해당하고 이를 조작하는 것이다. 



#### DOM 객체의 상속 구조

![DOM 객체의 상속 구조.png](./WEB.assets/DOM%20%EA%B0%9D%EC%B2%B4%EC%9D%98%20%EC%83%81%EC%86%8D%20%EA%B5%AC%EC%A1%B0.png)

image from velog.io/@niyu



* EventTarget
  
  * Event Listener를 가질 수 있는 객체가 구현하는 DOM 인터페이스

* Node
  
  * 여러 DOM 타입들을 상속하는 인터페이스

* Element
  
  * Document 안의 모든 객체가 상속하는 가장 범용적인 인터페이스
  
  * 부모인 Node와 그 부모인 EventTarget의 속성을 상속받는다. 

* Document
  
  * 브라우저가 불러온 웹 페이지를 보여준다. 
  
  * DOM 트리의 **진입점**(entry point) 역할을 수행한다. 

* HTMLElement
  
  * 모든 종류의 HTML 요소이다. 
  
  * 부모 element의 속성 상속한다. 



## DOM 선택 관련 메서드 (Select)

* .querySelector(selector)
  
  * 하나의 element를 선택한다. 
  
  * CSS selector를 만족하는 첫 번째 element 객체를 반환한다. (없으면 null)
    
    * 단일 element를 반환한다.
  
  * id, class,tag 선택자 등 모두 사용 가능하므로, 더 구체적이고 유연하게 선택 가능하다.
  
  

* .querySelectorAll(selector)
  
  * 여러 element를 선택한다. 
  
  * 일치하는 **NodeList**를 반환한다. 
    
    * index로만 각 항목에 접근이 가능하다. 
    
    * 배열에서 사용하는 forEach 메서드 및 다양한 메서드 사용이 가능하다.
      
      * HTMLCollection은 불가능
    
    * querySelectorAll()에 의해 반환되는 NodeList는 Static Collection으로 실시간으로 반영되지 않는다. 
  
  * id, class,tag 선택자 등 모두 사용 가능하므로, 더 구체적이고 유연하게 선택 가능하다.
  
  

* getElementById(id)
  
  * 단일 element를 반환한다. 



* getElementsByTagName(name)
  
  * HTMLCollection을 반환한다. 
    
    * name, id, index 속성으로 각 항목에 접근이 가능하다. 



* getElementsByClassName(names)
  
  * HTMLCollection을 반환한다.
    
    * name, id, index 속성으로 각 항목에 접근 가능하다. 



* Live Collection
  
  * 문서가 바뀔 때 실시간으로 업데이트된다. 
  
  * DOM의 변경사항을 실시간으로 collection에 반영한다. 
  
  

* Static Collection (non-live)
  
  * DOM이 변경되어도 collection 내용에는 영향을 주지 않는다. 
  
  * querySelectorAll()의 반환인 NodeList만 static collection에 해당한다. 





## DOM 변경 관련 메서드 (Creation)

* document.createElement()
  
  * 작성한 태그 명의 HTML 요소를 생성하여 반환한다. 



* Element.append()
  
  * 부모 Node의 자식 NodeList 중 마지막 자식 다음에 Node 객체 / DOMString을 삽입한다. 
  
  * 여러 개의 Node 객체, DOMString을 추가 할 수 있다.
  
  * 반환 값이 없다. 

* Node.appendChild()
  
  * 하나의 Node를 특정 부모 Node의 자식 NodeList 중 마지막 자식으로 삽입한다. 
    
    * Node만 추가가 가능하다. 
    
    * 1번 1개의 node만 추가 가능



### ParentNode.append() &  Node.appendChild()

#### ParentNode.append()

* DOMString 객체를 추가할 수 있다. 

* 반환 값이 없다. 

* 여러 Node 객체와 문자열을 추가할 수 있다. 

#### Node.appendChild()

* Node만 추가가 가능하다. 

* 추가된 Node 객체를 반환한다. 

* 하나의 Node 객체만 추가할 수 있다. 



DOM 변경 – 변경 관련 속성 (property)




### DOM 변경 관련 속성 (Property)

* • Node.innerText
  
  * Node 객체와 그 자손의 텍스트 컨텐츠(DOMString)를 표현한다. 
  
  * 사람이 읽을 수 있는 요소만 남긴다. 
  
  * 즉, 줄 바꿈을 인식하고 숨겨진 내용을 무시하는 등 최종적으로 스타일링이 적용된 모습으로 표현한다. 



* • Element.innerHTML
  
  * 요소(element) 내에 포함된 HTML 마크업을 반환한다.
  
  * XSS 공격에 취약하다. 



### DOM 삭제 관련 메서드

* ChildNode.remove()
  
  * Node가 속한 트리에서 해당 Node를 제거한다. 

* Node.removeChild()
  
  * 자식 Node를 제거하고 제거된 Node를 반환한다. 



### DOM 속성 관련 메서드

* • Element.setAttribute(name, value)
  
  * 요소의 값을 설정한다. 
  
  * 이미 존재하는 값이면 값을 갱신하고, 존재하지 않으면 새 속성으로 추가한다. 



* • Element.getAttribute(attributeName)
  
  * 해당 요소의 값을 반환한다. 
  
  * 인자는 값을 얻고자 하는 속성의 이름이다. 



## BOM, Browser Object Model

* 브라우저와 소통하기 위한 모델

* 브라우저의 창이나 프레임을 추상화해서 프로그래밍적으로 제어할 수 있도록 한다. 

* window 객체는 모든 브라우저로부터 지원받으며 브라우저의 창(window)를 지칭한다. 





# addEventListener

```js
const buttons = document.querySelectorAll('button');

for (const button of buttons) {
  button.addEventListener('click', createParagraph);
}

```

`querySelectorAll()` 함수를 사용하면 현재 페이지 내의 모든 버튼을 선택할 수 있다. 

반복문과 함께 `addEventListener()`로 여러 버튼에 하나씩 동작 기능(handler)을 넣어준다. 


