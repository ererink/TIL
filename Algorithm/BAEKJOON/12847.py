# 꿀 아르바이트
# 슬라이딩

'''
n = 월세 내기 바로 전날, list 요소의 개수
m = 일 할 수 있는 날, 리스트에서 m개 선택 가능
'''
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
days = list(map(int, input().split()))


cnt = 0
max_cnt = 0

for i in range(n - 2):
    cnt = 0
    for j in range(m):
        cnt += days[i + j]
    if cnt > max_cnt:
        max_cnt = cnt

print(max_cnt)