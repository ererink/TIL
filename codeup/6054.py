# 2개의 정수값이 입력될 때,
# 그 불 값이 모두 True 일 때에만 True 를 출력하는 프로그램을 작성해보자.

a, b = map(int, input().split())

print(bool(a) and bool(b)) # and을 사용하여 '모두 True일 때의' 조건을 만들어준다. 