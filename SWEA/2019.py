# 1부터 주어진 횟수까지 2를 곱한 값(들)을 출력하시오.

# 주어질 숫자는 30을 넘지 않는다.

# 내 답안 
n = int(input())
mul = []

for i in range(1, n + 1):
    mul = i * 2  # 출력 값이 쌓여서 차례대로 출력하는 것이 아닌 값이 갱신된다. 
    if i > 30:
        break
print(mul, end = ' ')

## 모범 답안
n = int(input())

for i in range(0, n + 1):
    print((2**i), end = ' ') # 바로 출력해주어서 출력 값이 차례대로 나올 수 있게 한다. 
                             # 2**i는 2에 i를 제곱한다. 
