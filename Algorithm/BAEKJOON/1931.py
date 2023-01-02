'''
회의실 배정

input = 11
        1 4
        3 5
        0 6
        5 7
        3 8

        5 9
        6 10
        8 11
        8 12
        2 13
        12 14

output = 4

(1,4), (5,7), (8,11), (12,14)

- 최대한 짧은 시간
- 끝나는 시간 순서로 정렬
'''

from heapq import heappop, heappush

n = int(input())

times = []
for i in range(n):
    s, e = map(int, input().split())
    heappush(times, (e, s))     # 끝 시간, 시작시간 순으로 넣기

cnt = 0     # 계속 할당되는 끝 시간
answer = 0  # 빌릴 수 있는 회의실 개수
while times:
    a, b = heappop(times)
    if b >= cnt:    # 끝 시간과 다음 튜플의 시작 시간 비교
        cnt = a
        answer += 1

print(answer)