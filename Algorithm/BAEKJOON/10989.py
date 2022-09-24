# 0부터 10001까지의 리스트를 만든다. 
# 입력값이 인덱스가 된다. 
# 인덱스 번호때문에 10001
import sys

n = int(sys.stdin.readline())
a = [0] * 10001

for _ in range(n):
    a[int(sys.stdin.readline())] += 1

for j in range(10001):
    if a[j]:
        for k in range(a[j]):
            print(j)