# N줄덧셈
# 1부터 주어진 숫자만큼 모두 더한 값을 출력하시오.

n = int(input())
result = 0

for i in range(1, n + 1):
    result += i

print(result)