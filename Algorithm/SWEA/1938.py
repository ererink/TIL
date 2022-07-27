# 아주 간단한 계산기
# 두개의 입력값을 사칙연산 + - * / 순서대로 연산한 결과를 출력한다. 

# (소수점 이하 버리기)

a, b = map(int, input().split())

print(a + b)
print(a - b)
print(a * b)
print(a // b)