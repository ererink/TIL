#2개의 정수값이 입력될 때,
# 그 불 값(True/False) 이 모두 False 일 때에만 True 를 출력하는 프로그램을 작성해보자.

a, b = map(int, input().split())
c = bool(int(a))
d = bool(int(b))

if (a == False and b == False):
    print("True")
else:
    print("False")