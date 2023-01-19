# 치킨 배달

import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
house = []
chicken = []
answer = 999999                                     # 최종 치킨 거리 비교
for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            house.append([i, j])
        elif maps[i][j] == 2:
            chicken.append([i, j])


for c in combinations(chicken, m):                  # 최대 m개의 조합으로 
    distance = 0
    for h in house:
        c_dis = 999
        for j in range(m):
            c_dis = min(c_dis, abs(h[0] - c[j][0]) + abs(h[1] - c[j][1]))   # 치킨거리 계산 후 더 거리가 짧은 치킨거리 할당
        distance += c_dis                                                   # 각 최단 치킨거리 더해주기

    answer = min(answer, distance)

print(answer)