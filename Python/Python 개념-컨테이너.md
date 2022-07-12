## 컨테이너

* 시퀀스

  * 리스트, 문자열, 튜플, 레인지

  * 순서가 있다

    [2, 0, 1] -> 정렬은 되어있지 않지만 순서는 있다. 

  * 인덱스, 슬라이싱, x in s(항목에 있는지 확인(true/false)), 최댓값과 최솟값(sum, max, min)

* 컬렉션/비시퀀스

  * 세트, 딕셔너리 
  * 순서가 없다



```python
print([1, 2] + [3])
# 출력
[1, 2, 3]
```



## 시퀀스형 컨테이너 (Sequence Container)

### 리스트(List)

* 변경 가능한 값들의 나열된 자료형이다.
* 순서를 갖는다.
* 서로 다른 타입의 요소를 가질 수 있다. 
* 반복 가능하다.
* [0, 1, 2, 3]의 형태



```python
# 리스트 생성
my_list = []
another_list = list()
type(my_list)
# <class 'list'>
type(another_list)
# <class 'list'>
```



### 리스트 값 추가 및 삭제

* .append() : 맨 뒤에 추가하는 것이다. 

* .pop() : 삭제



```python
boxes = ['apple', 'banana']

len(boxes) # 2; 길이(개수)를 뜻함
boxes[1] # banana (apple은 0)
boxes[1][0] # 인덱스 1의 0번째 글자는? 'b'
```





## 튜플

* 불변한 값들의 나열
  * 값을 바꿀 수 없다. 추가/삭제도 불가능하다.
* 반복 가능하다
* a = (0, 1, 2, 3)의 형태를 가짐



## 레인지 (Range)

* 숫자의 순서를 담고있다

```python
range(3)
-> 0, 1, 2

range(1, 4)
-> 1, 2, 3 # 1이상 4미만

range(1, 5, 2) # 1 이상 5미만, 2만큼 증가 (슬라이싱)
-> 1, 3
```





## 비시퀀스 컨테이너 (컬렉션) (Associative Container)

## 세트 (집합)

* 유일한 값들의 모음(collection)
* 중복된 값이 없기 때문에 **순서가 없다.** 
* 변경 가능, 반복 가능 
* .add, .remove()



## 딕셔너리

* 키와 값 쌍으로 이뤄진 모음이다. (key-value)
  * 키: 변경 불가능한 데이터만 활용 가능하다.
    * 리스트가 들어갈 수 없다.
  * 값: 어떠한 형태든 관계 없다.
    * 리스트가 들어갈 수 있다.
* 변경 가능하며 반복 가능하다 (mutable, utterable)



.split: 문자열을 특정 단위로 쪼개준다.

```python
a = '10:20'
numbers = a.split(':') # :을 기준으로 쪼개라!
print(numbers)
	# 출력
  ['10', '20']

# 출력할 때 sep(seperator)를 작성하면 값 사이에 해당 문자를 넣어서 출력한다.
print(numbers[0], numbers[1], sep='****')
	# 출력
  ['10',****,'20']
```

