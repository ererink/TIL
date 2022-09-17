'''
각 동전의 개수는 무한대
'''

n, k = map(int, input().split())
coins = []

for _ in range(n):
    coins.append(int(input()))

coins.sort(reverse = True)
answer = 0
for i in coins:
    if i > k:
        continue
    
    answer += k // i
    k %= i
    if k == 0:
        break

print(answer)

    