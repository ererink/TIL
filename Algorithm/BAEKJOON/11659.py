# 구간 합 구하기 4

'''
5 3         => 수의 개수, 합을 구해야 하는 횟수
5 4 3 2 1   => 수
1 3         => 합을 구해야 하는 구간
2 4
5 5
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
cnt = 0
temp = [0]

# 다 더하기 
for i in nums:
    cnt += i 
    temp.append(cnt)

for j in range(m):
    a, b = map(int, input().split())
    print(temp[b] - temp[a - 1])

