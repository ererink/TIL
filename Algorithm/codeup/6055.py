# 2개의 정수값이 입력될 때,
# 그 불 값이 하나라도 True 일 때에만 True 를 출력하는 프로그램을 작성해보자.

a, b = map(int, input().split())

print(bool(a) or bool(b)) # or을 이용하여 '하나라도'의 조건을 충족해준다. 