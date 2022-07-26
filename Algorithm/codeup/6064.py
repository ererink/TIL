# 입력된 세 정수 a, b, c 중 가장 작은 값을 출력하는 프로그램을 작성해보자.
# 단, 3항 연산을 사용한다.

a, b, c = map(int, input().split())
print(min(a, b, c))

# 모범 답안
a, b, c = input().split()
a = int(a)  #변수 a에 저장되어있는 값을 정수로 바꾸어 다시 변수 a에 저장
b = int(b)
c = int(c)

d = a if a<b else b
e = d if d<c else c

print(e)
