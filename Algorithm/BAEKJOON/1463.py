'''
1로 만들기 (DP)

X가 3으로 나누어 떨어지면, 3으로 나눈다.
X가 2로 나누어 떨어지면, 2로 나눈다.
1을 뺀다.

- 1을 빼는 경우 / 2로 나누는 경우 / 3으로 나누는 경우 중 최솟값 찾기
=> Memoization 메모이제이션: 동일한 계산을 반복해야 할 때, 이전에 계산한 값을 메모리에 저장
'''
n = int(input())
d = [0] * (n + 1)

for i in range(2, n + 1): 
    d[i] = d[i - 1] + 1
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)

print(d[n])

'''
# DP 모르고 푼 방법 (실패)
x = int(input())

cnt = 0
while x != 1:
    if (x - 1) % 3 == 0:
        x = x - 1
        cnt += 1 
        
    if x % 3 == 0:
        x = x / 3 
        cnt += 1
        print(x)
    elif x % 2 == 0:
        x = x / 2
        cnt += 1
        print(x)

    else:
        x = x - 1
        cnt += 1
        print(x)

print(cnt)
'''
