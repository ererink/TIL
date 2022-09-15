# Javascript 문법

## 

## 기본 형식

```js
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>

  <!-- JS 코드를 작성하는 영역 -->
  <script>
    console.log('hello, js!')
    
    const title = document.createElement('h1')  // h1 요소(element)를 만든다.
    
    title.innerText = 'JS 기초' 				  //title에 'JS 기초' 텍스트를 추가한다. 
    
    const body = document.querySelector('body') // 선택자로 body태그를 가져와서
    
    body.appendChild(title)						// body태그에 자식 요소로 추가한다. 
  </script>
</body>
</html>
```

body의 마지막 부분에 자바스크립트를 적어준다.



### 선언

- var
- let
- const



### 변수

- 변수를 식별자(idenrifiers)로 사용한다.
- const, let, var로 변수를 선언한다. 
- var, let으로 선언된 변수가 초기 값이 없다면 undefined 값을 갖는다.



```js
var a;
console.log('a 값은 ' + a); // a 값은 undefined

let x;
console.log('x 값은 ' + x); // x 값은 undefined
```



그래서 undefined을 사용하여 변수 값이 존재하는지 확인할 수 있다.

```js
var input;
if(input === undefined) {
  doThis();
} else {
  doThat();
}
```



변수의 범위가 존재한다. (전역변수, 지역변수)

```js
if (true) {
  var x = 5;
}
console.log(x); // 5
```

x의 scope가 전역변수이기 때문에 5 값을 반환할 수 있다. 

x의 scope는 if문 블록 내에서만 제한되지 않는다.



```js
if (true) {
  let y = 5;
}
console.log(y); // ReferenceError: y is not defined
```

let을 사용하면 값이 반환되지 않는다.



## const

- 값을 바꾸거나 재선언할 수 없다. 이를 위해서 값을 초기화해야 한다. 
- const의 scope는 let의 scope와 같다. 
- 같은 scope에 있는 함수나 변수의 동일한 이름을 선언할 수 없다.

```js
// 오류 발생
function f() {};
const f = 5;

// 오류 발생
function f() {
  const g = 5;
  var g;

  //statements
}
```

### 



### 자료형 변환

```js
var answer = 42;


answer = 'Thanks for all the fish...';
```

다음과 같이 변수를 정의한 후,

동일한 변수에 문자열 값을 할당할 수 있다.

JavaScript는 동적 언어이므로, 위 할당은 오류 메시지가 발생하지 않는다.





```js
x = 'The answer is ' + 42 // "The answer is 42"
y = 42 + ' is the answer' // "42 is the answer"
```

문자열과 정수를 '+'로 합쳐서 x, y에 할당할 수 있다.



```js
'37' - 7 // 30
'37' + 7 // "377"
```

문자열을 정수로 바꾸지 않아도 정상적으로 계산이 실행된다.



### 

### 문자열 → 정수

- parselnt()
  - 정수만 반환한다.
- parseFloat()
  - 소수를 반환할 수 있다.

```js
'1.1' + '1.1'          // '1.11.1'

(+'1.1') + (+'1.1')    // 2.2
```

괄호에 따라 값이 달라진다.



## 배열 리터럴 Array literals

```js
let fish = ['Lion', , 'Angel'];
```

fish[0]은 "Lion", fish[1]은 undefined, fish[2]는 "Angel" 값을 반환한다.





## **조건문**

### if...else문

```js
if (condition_1) {
  statement_1;
} else if (condition_2) {
  statement_2;
} else if (condition_n) {
  statement_n;
} else {
  statement_last;
}
```

if, else if, else로 조건문을 생성한다.



```js
if (condition) {
  statement_1_runs_if_condition_is_true;
  statement_2_runs_if_condition_is_true;
} else {
  statement_3_runs_if_condition_is_false;
  statement_4_runs_if_condition_is_false;
}
```

if 문을 중첩할 때 블록문을 함께 사용한다.



### switch문

```js
switch (expression) {
  case label_1:
    statements_1;
    break;
  case label_2:
    statements_2;
    break;
    …
  default:
    statements_default;
}
```

case의 값을 비교하여 일치하는 case 명령문을 실행한다. 

일치하는 값을 찾지 못했다면 default 절을 탐색한다. 

default 절에서 일치하는 값을 찾지 못했다면 관련된 명령문을 실행한다.



```js
switch (fruittype) {
  case '오렌지':
    console.log('오렌지는 파운드 당 $0.59입니다.');
    break;
  case '사과':
    console.log('사과는 파운드 당 $0.32입니다.');
    break;
  case '바나나':
    console.log('바나나는 파운드 당 $0.48입니다.');
    break;
  case '체리':
    console.log('체리는 파운드 당 $3.00입니다.');
    break;
  case '망고':
    console.log('망고는 파운드 당 $0.56입니다.');
    break;
  case '파파야':
    console.log('망고와 파파야는 파운드 당 $2.79입니다.');
    break;
  default:
    console.log(`죄송합니다. ${fruitType}은 품절입니다.`);
}
console.log('더 필요한게 있으신가요?');
```

break를 사용하여 해당 값을 찾은 후 switch문을 종료하고 다음 명령문을 실행하도록 한다.





### throw문

예외처리를 위해서 throw문을 사용한다.

```js
throw 'Error2'; // String
throw 42; // Number
throw true; // Boolean
throw {
  toString: function () {
    return '저는 객체예요';
  },
};
```



### try ... catch문

```js
function getMonthName(mo) {
  mo = mo - 1; // 배열 인덱스에 맞춰 월 조절 (1 = Jan, 12 = Dec)
  let months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
  if (months[mo]) {
    return months[mo];
  } else {
    throw 'InvalidMonthNo'; // 여기서 throw 키워드 사용
  }
}

try {
  // 시도할 명령문
  monthName = getMonthName(myMonth); // 예외가 발생할 수 있는 함수
} catch (e) {
  monthName = 'unknown';
  logMyErrors(e); // 오류 처리기에 예외 객체 전달
}
```

try문에 실행할 명령문을 적고, 그 안에서 예외가 발생할 경우 처리를 맡을 하나 이상의 반응 명령문을 지정한다. 

예외가 발생하면 catch 문을 실행한다.



```js
try {
  throw 'myException'; // 예외 생성
} catch (e) {
  // 모든 예외를 처리하기 위한 명령문
  logMyErrors(e); // 오류 처리기에 예외 객체 전달
}
```


