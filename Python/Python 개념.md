### 컴퓨터란 (Computer)?

Caculation + Remember의 합성어로 

'계산을 하고 기억을 한다' 라는 뜻을 갖고 있다. 



### 프로그래밍이란 (Programming)?

명령어의 모음 (집합)이다.

즉, 프로그래밍은 명령어를 만드는 행위이다. 

#### 언어란?

생각을 나타내고 전달하기 위해 사용하는 체계, 문법적으로 맞는 말의 집합



### 그럼 컴퓨터 언어란?

컴퓨터에게 생각을 나타내고 전달한다. 

컴퓨터에게 명령하기 위한 약속인 것이다. 



컴퓨터 언어와 관련된 두 가지 지식이 있다. 

선언적 지식 (declarative knowledge): 사실에 대한 내용

**명령적 지식 (imperative knowledge): 'How to'**

컴퓨터 언어를 쓰기에 앞서 우리는 이제 '명령적 지식'을 사용해야 한다. 





## 파이썬이란?

다른 프로그래밍 언어보다 문법이 간단하면서도 엄격하지 않다. 

* 변수에 별도의 타입 지정을 요구하지 않는다. 

문법 표현이 매우 간결하다. 

* 중괄호 {} 대신 들여쓰기를 사용한다. 



### 특징

* 인터프리터 언어 
  * 코드를 컴파일(기계어로 변환) 과정 없이 바로 실행 가능하다. 
  * 코드를 입력하고 실행하여 바로 확인할 수 있다. 
* **객체 지향 프로그래밍 (Object Oriented Programming)**
  * 파이썬은 객체지향 언어이며, 모든 것이 객체로 구현되어 있다. 
    * 객체: 숫자, 문자, 클래스, 물건 / 대상, ~것



## 변수란 (variable)?

* 메모리에 저장되어 있는 객체를 참조하기 위해 사용되는 이름 (a = 8)

  * 객체: 숫자, 문자, 클래스 등 값을 가지고 있는 모든 것

    즉, 참고하는 객체가 바뀔 수 있기 때문에 변수라고 부른다. 

* 변수는 할당 연산자(=)를 통해 값을 할당한다. 

  * 수학에서의 '같다'가 아니라 '할당한다' 라고 생각해야 한다. 



예를 들어, 'Happy Coding'을 5번 출력해보자. 

``` python
print ('Happy Coding')
print ('Happy Coding')
print ('Happy Coding')
print ('Happy Coding')
print ('Happy Coding')

hello = 'Happy Coding'
print(hello)
print(hello)
print(hello)
print(hello)
print(hello)
```

'Happy Coding'을 다른 말로 바꾼다면 5번 혹은 더 이상으로 손이 간다. 일일이 고쳐야 한다는 큰 단점이 있다.

하지만, 반복적으로 쓰는 값을 변수로 할당하여 사용한다면 더욱 편리하게 사용할 수 있다. 

### 변수, 할당 연산자

type(): 변수에 할당된 값의 타입

id(): 변수에 할당된 값의 고유한 identity 값.



코드는 위에서부터 아래로 실행된다. 

오른쪽에서 왼쪽으로 실행된다. 



## 식별자(Identifiers)

객체를 식별하는데 사용하는 이름이다. 

#### 규칙

* 첫 글자에 숫자 X
* 이미 존재하는 키워드(함수 등 명령어)는 예약어로 사용 X
* 영어, 숫자, 언더스코어(_)로 명명함
* 길이 제한이 없음
* 대소문자를 구별함



### 사용자 입력

`input()` 

* 값을 즉시 입력 받을 수 있는 내장함수이다. 
* **반환값은 항상 문자열의 형태로 반환한다.** 



### 주석(Comment)

* 코드에 대한 설명이다. 
* 컴퓨터는 주석을 인식하지 못한다. 
* 주석을 작성하는 습관이 중요하며, 이는 높은 이해와 코드 분석을 위함이다. 



```python
# 샵(#)을 사용하여 주석을 이용한다.
```





## 파이썬 기본 자료형

* Boolean Type
* Numeric Type
  * Int (정수)
  * Float (실수)
  * Complex (복소수)
* String Type
* None: 값이 없음을 표현



## Boolean

* Ture, False 값을 갖는다.
* 비교, 논리 연산에 쓰인다. 
* 0, 0.0, (), [], {}, None 은 모두 False 값이 반환된다. 



```python
bool(0) # False
bool('') # False
bool([]) # False
bool(1) # True
bool(-1) # True
bool([1, 2, 3]) # True

```



### 논리 연산자

True와 False를 반환한다.

A and B

* A와 B 모두 True여야 True이다.

A or B

* A나 B 둘 중 하나만 True여도 True이다
* A와 B 모두 False여야 False이다.

Not

* True를 False로, False를 True로
* not True == False, not False == True



## Numeric Type (수치형)

### 정수(Int)

* 모든 정수의 타입은 int이다. 
* 매우매우 큰 수를 나타내도 오버플로우가 발생하지 않는다. 

### 실수(Float)

* 모든 실수는 float 타입이다. 
* 컴퓨터는 2진수로 숫자를 표현하기 때문에 floating point rounding error가 발생한다. 

​		(3.14 - 3.02 == 0.12

​		0.12가 나오지 못하고 0.12000000001이 나온다.)

### 복소수 (Complex)

* 실수부와 허수부로 구성되었다.



### 산술 연산자

**% 나머지** -> 생각보다 많이 쓰인다. 짝수나 홀수 확인할 때 많이 쓰인다. 

​				3의 배수 알아볼 때, 3으로 나눴을 때 나머지가 0이다, 2의 배수는 짝수이다 등등

/ 나눗셈

// 몫

** 거듭제곱 

a = a + 1 을 a += 1로 표현할 수 있다. 

### 비교 연산자

* == 같음  ('='은 할당 연사자이다.)
* != 같지 않음



## 문자열(String Type)

* 모든 문자는 str 타입이다.

* 작은 따옴표('')나 큰 따옴표("")를 쓴다. 

### 중첩따옴표 (Nested Quotes)

* 따옴표 안에 따옴표

```python
print('She said "helloooo"')
print("She said 'helloooo')
# 삼중 따옴표 (Triple Quotes)
print('''"She said 'helloooo'''')
```



### 인덱싱

* 위치를 통해 값을 찾는다.

```python
fruit = 'abcde'

# 슬라이싱
print(fruit[1:3])
# 1부터 3미만의 값을 출력한다. 

s[2:6:2] -> 2부터 5까지 2씩 건너서 출력해줘

s[::] 처음부터 끝까지 1씩 (그대로)
s[::-1] 처음부터 끝까지 -1씩 (거꾸로)

```

```python
# 결합(Concatenation)
'hi,' + 'erin' # 'hi, erin'

# 반복(Repetition)
'hi' * 3 #'hihihi'

# 포함(Membership)
'e' in 'erin' # True
't' in 'erin' # False
```



#### Escape sequence

문자열 내에서 문자나 조작을 위해 역슬래시(\\)를 사용하여 구분한다. 

* \n : 줄바꿈
* \t : 탭
* \0
* \\\ : `\`

```python
print('안녕하세요,\n반갑습니다.')

# 출력
안녕하세요,
반갑습니다.

# 따옴표
print("따옴표를 '씁니다'")
print('따옴표를 \'씁니다\'')

print('escape sequence는 역슬래시 \\를 활용합니다.')
# 출력
escape sequence는 역슬래시 \를 활용합니다.
```

\ \: '나 지금 따옴표 쓰는거 아니야!'



#### String interpolation

```python
# 문자열 안에 변수 넣기
score = 100

# 내 점수는 100이야.
print('내 점수는 ' + score + '이야.')
 # 오류 발생: score가 int이기 때문에 

print(f'내 점수는 {score}이야.')
# 출력
	내 점수는 100이야.
```



## 자료형 변환

* 암시적
  * 파이썬이 바꿔주는 것
* 명시적
  * 내가 직접 의도적으로 바꾸는 것



숫자와 문자는 더할 수 없어서 직접 문자열로 변환하는 것이다. 

```python
print('내 점수는 ' +str(score) + '이야.')
```



## 컨테이너(Container)

* 여러 개의 값을 담을 수 있는 것이다.
* 리스트로 담아낸다.

```python
name = '동현'
name1 = '효근'
name2 = '수경'
name3 = '나영'
name4 = '다겸'
name5 = '예지'

# 리스트
students = ['동현', '효근', '수경', '나영', '다겸', '예지']
# 동현 찾기
print(students[0])
# 예지 찾기
print(students[-1])

# 회차 별로 나누기 
students_1= ['동현', '효근']
students_2= ['수경', '나영']
students_3= ['다겸', '예지']

	# 딕셔너리 (사전)
	students = {
    '1회차': ['동현', '효근'], 
  	'2회차': ['수경', '나영'],
  	'3회차': ['다겸', '예지']
  }
  # 1회차 찾기
  print(students['1회차'])
```

리스트는 값들의 나열(배열, sequence)이다. 그렇기 때문에 **순서**로 접근한다. 

딕셔너리는 키와 값의 쌍이기 때문에 **키**로 접근을 한다. (순서가 없다)