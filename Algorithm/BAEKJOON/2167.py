# 2차원 배열의 합

n, m = map(int, input().split())

maps = [list(map(int, input().split())) for _  in range(n)]

k = int(input())

for _ in range(k):
    i, j, x, y = map(int, input().split())
    i -= 1; j -= 1;
    cnt = 0
    for q in range(i, x):
        for w in range(j, y):
            cnt += maps[q][w]
    print(cnt)