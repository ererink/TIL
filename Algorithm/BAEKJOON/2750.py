# 수 정렬하기
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

import heapq

N = int(input())
heap = []

for _ in range(N):
    n = int(input())
    heapq.heappush(heap, n)
    
for i in range(len(heap)):
    print(heapq.heappop(heap))