# Javascript 문법 3

## **조건문**

### if

- 결과값을 Boolean 타입으로 변환 후 참/거짓을 판단한다. 
- 중괄호 안에 작성한다. 

```js
const nation = 'Korea'

if (nation === 'Korea') {
    console.log('안녕하세요')
} else if (nation === 'Farance') {
    console.log('Bonjour')
} else {
    console.log('Helloo')
}
```

### switch

- 결과값이 어느 값(case)에 해당하는지 판별한다. 
- 조건이 많아질 경우 if문보다 가독성이 나을 수 있다. 
- 표현식의 결과값과 case문의 오른쪽 값을 비교한다.
- break, defaul는 선택적으로 사용 가능하다.
- break문을 만나지 못하면 case, default문이 모두 출력된다.

```js
const nation = 'Korea'

switch (nation) {
    case 'Korea': {
    console.log('안녕하세요')
    } 
    case 'France': {
    console.log('Bonjour')
    }
    default: {
    console.log('Helloo')
    }
  }
```

break문이 없기 때문에 3개의 값 모두 출력된다. 

### 반복문

- while
  - 조건은 소괄호 안에 작성한다. 
  - 실행할 코드는 중괄호 안에 작성한다.
  - 블록 스코프 생성한다. 

```js
let i = 0

while (i < 6) {
    console.log(i)    // 0, 1, 2, 3, 4, 5
        i += 1
}
```

- for
  - ;로 구분되는 세 부분으로 구성
  - initialization
    - 최초 반복문 진입 시 1회만 실행한다. 
  - condition
    - 조건문, 매번 반복 전에 평가되는 부분이다. 
  - expression
    - 매 반복 시행 이후 평가되는 부분이다. 
  - 블록 스코프를 생성한다. 

```js
for (let i = 0; i < 6; i++) {
    console.log(i)    // 0
}
```

i가 6이 될 때 까지 condition과 expression을 반복한다. 

- for ... in
  - 객체의 속성들을 순회할 때 사용한다.
  - 키-값으로 이루어진 자료구조이다.
  - 배열 순회도 가능하지만 비추!

```js
const capitals = {
    korea: 'seoul',
    france: 'paris',
    USA: 'washington D.C.'
}

for (let capital in capitas) {
    console.log(capital) 
}    
//    korea, france, USA
```

키값이 반환된다. 

- for .. of
  - 반복 가능한 객체 순회이며, 값을 꺼낼 때 사용한다. 
  - of와 in의 차이 
    - of: 객체를 조작한다면 오류가 발생한다. 배열 순회가 적합하다.
    - in: 인덱스 번호가 나온다. 객체 순회가 적합하다.

```js
const fruits = ['딸기', '바나나', '메론']

for (let fruit of fruits) {
    fruit = fruit + '!'
    console.log(fruit)
}
```

### 함수

- 표현식 내에서 정의하는 방식
- 함수의 이름을 생략하고 익명 함수로 정의가 가능하다. 
  - 익명 함수는 함수 표현식에만 가능하다. 

#### 함수 정의

- name: 함수 이름
- args: 매개변수
- body: 중괄호 내부

```js
function name(args) {
    codeeeee
}

function add(num1, num2) {
   return num1 + num2
}

add(1, 2)
```

#### 함수 표현식

- 변수에 저장하는 것처럼 사용한다. 
- 익명함수로 정의가 가능하다. 익명함수
- 함수 그 자체를 변수에 저장하는 느낌이다.

```js
function name = function (args) {    codeeeee
}

function add = function (num1, num2) {   return num1 + num2
}

add(1, 2)
```

#### 매개변수와 인자의 개수 불일치를 허용한다.

- 파이썬은 정해진 개수만 넘길 수 있었다.
- 자바스크립트는 매개변수와 인자의 개수에 제약이 있지 않다. 넘길 수 있다.
  - 알아서 개수를 맞춰서 인자를 넘긴다.
  - 매개변수보다 인자의 개수가 적을 경우 undefinded을 넘긴다. 
  - '...' 을 쓰면 배열로 값을 받을 수 있다.

```js
const noArgs = function () {
    return 0
}

noArgs(1, 2, 3)
// 0

const twoArgs = function (arg1, arg2) {
    return [arg1, arg2]
}

twoArgs(1, 2, 3)
// [1, 2]
```

매개변수보다 인자의 개수가 많을 경우

```js
const threeArgs = function (arg1, arg2, arg3) {
    return [arg1, arg2, arg3]
}

threeArgs()            // [undefined, undefined, undefined]
threeArgs(1)        // [1, undefined, undefined]
threeArgs(1, 2)        // [1, 2, undefined]
```

매개변수보다 인자의 개수가 적을 경우

### Rest Parameter

- '...'를 사용하면 함수가 정해지지 않은 수의 매개변수를 배열로 받는다. 

```js
const restOpr = function (arg1, arg2, ...restArg) {
    return [arg1, arg2, restArgs]
}

restArgs(1, 2, 3, 4, 5)        // [1, 2, [3, 4, 5]]
restArgs(1, 2)                // [1, 2, []]
```

### Spread operator

- 배열 인자를 전개하여 전달한다. 

```js
const spreadOpr = function (arg1, arg2, arg3) {
return arg1 + arg2 + arg3
}
const numbers = [1, 2, 3]
spreadOpr(...numbers) // 6
```

함수 선언식: 익명 함수 기능이 불가능하며, 호이스팅이 가능하다. 

함수 표현식: 익명 함수 기능이 가능하며, 호이스팅이 불가능하다. 

### 호이스팅(hoisting) – 함수 선언식

- 함수 호출 이후에 선언 해도 동작한다. 

```js
add(2, 7)    // 9

function add (num1, num2) {
    return num1 + num2
}
```

함수 표현식으로 선언한 함수는 함수 정의 전에 호출 시 에러가 발생한다. 

함수 표현식으로 정의된 함수는 변수로 평가되어 변수의 scope 규칙을 따르기 때문이다. 

```js
sub(7, 2)    => Error

const sub = function (num1, num2) {
    return num1 - num2
}
```

## Arrow Function

- 간결하게 함수를 정의할 수 있다. 
- function 키워드가 생략된다. 
- => 표현을 쓴다.
- $ {   } 표현을 쓴다. 

```js
const arrow1 = function (name) {
return `hello, ${name}`
}
// 1. function 키워드 삭제
const arrow2 = (name) => { return `hello, ${name}` }

// 2. 매개변수가 1개일 경우에만 ( ) 생략 가능
const arrow3 = name => { return `hello, ${name}` }

// 3. 함수 바디가 return을 포함한 표현식 1개일 경우에 { } & return 삭제
가능
const arrow4 = name => `hello, ${name}`
```

### 문자열

- includes
- split
- replace
  - replaceAll
- trim
  - 파이썬은 strip

### 배열

- reverse
- push
- pop
- shift / unshift
- includes
- indexOf
- join
  - 파이썬은 문자열 매서드이지만, 자바스크립트는 배열의 매서드이다
- length
  - 배열의 길이

### Array Helper Methods

### **forEach**

• array.forEach(callback(element[, index[,array]]))

- 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행한다. 
- 콜백 함수를 인자로 받는다.
- 콜백함수는 함수를 나중에 다시 호출할 함수이다.
  - 함수 그 자체를 인자로 받는다.
  - 파이썬의 map 함수의 int가 입력값을 하나씩 넣어주는 것과 같다. 여기서 int는 함수이다.
- 콜백함수는 3가지 매개변수로 구성된다.
  - element: 배열의 요소
  - index: 배열 요소의 인덱스
  - array: 배열 자체

```js
const fruits = ['딸기', '수박', '사과', '체리']
fruits.forEach((fruit, index) => {
console.log(fruit, index)
    // 딸기 0
    // 수박 1
    // 사과 2
    // 체리 3
})
```

### map

- 콜백 함수를 한 번씩 실행한다. 
- 콜백 함수의 반환 값을 요소로 하는 새로운 배열 반환한다. 
- 기존 배열을 다른 형태로 바꿀 때 유용하다. 

```js
const numbers = [1, 2, 3, 4, 5]

const doubleNums = numbers.map((num) => {
    return num * 2
})

console.log(doubleNums)        // [2, 4, 6, 8, 10]
```

### filter

- 콜백 함수를 한 번씩 실행한다. 
- 콜백 함수의 반환 값이 true인 것만 반환한다. 
- 기존 배열의 요소들을 필터링할 때 유용하다. 

```js
const numbers = [1, 2, 3, 4, 5]

const oddNums = numbers.filter((num, index) => {
    return num % 2
})

console.log(oddNums)        // 1, 3, 5
```

### reduce

- 누적되는 변수의 값을 총계를 내고자 할 때 사용한다. (acc)
- 주요 매개변수
  - acc: 이전 callback 함수의 반환 값이 누적되는 변수
  - initialValue: 최초 callback 함수 호출 시 acc에 할당되는 값, default 값은 배열의 첫 번째 값 (선택사항)
    - 빈 배열의 경우 initialValue를 제공하지 않으면 에러가 발생한다. 

```js
const numbers = [1, 2, 3]

const result = numbers.reduce((acc, num) => {
    return acc + num
}, 0)

console.log(result)        // 6
```

## 객체

- 속성의 집합이다. 
- 중괄호 내부에 key와 value의 쌍으로 표현한다. 
- 파이썬의 딕셔너리
- 키는 문자열 타입만 가능하다. 
  - 키에 따옴표가 없다.
  - 값은 모든 타입(함수포함) 가능하다. 
- 객체에서 매서드는 함수인 경우 메서드라고 한다.
- 메서드로 화살표 함수를 쓰지 않는다.
  - getName: ( ) => this.name

```js
const me = {
    firstName: 'John',
    lastName: 'Doe’    ,    getFullName: function () {    return this.firstName + this.lastName    }}
```

```js
const btn1 = document.querySelector('#btn1')

btn1.addEventListener('click', funtion() {        // 콜백함수, btn1이 클릭되면 함수를 실행한다. 

    const h1 = document.querySelctor('h1')        // h1태그를 선택해서 

    h1. classList.toggle('blue')                // 클래스 blue를 토글한다. 

})
```

- '클릭하면 함수를 실행시킬게.'
- event가 발생하면 함수를 실행한다.
- 외부에 함수를 정의하고 함수의 이름을 적어도 문제가 없다.
- 함수가 인자이다.
- 클릭이 됐다 -> 함수를 실행시킨다.
