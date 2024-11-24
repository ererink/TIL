# 완전탐색

n, m = map(int, input().split())
arrays = []
for i in range(n):
    line = list(map(int, input().split()))
    arrays.append(line)

blocks = [
    [(0, 0), (0, 1), (0, 2)],   # ㅡ
    [(0, 0), (1, 0), (2, 0)],   # ㅣ
    [(0, 0), (1, 0), (1, 1)],   # ㄴ
    [(0, 0), (1, 0), (1, -1)],  # ㄴ 뒤집기
    [(0, 0), (0, 1), (1, 1)],  # ㄱ
    [(0, 0), (0, -1), (1, -1)],   # ㄱ 뒤집기
]

def block_calculate(x, y, blocks):
    total = 0
    for dx, dy in blocks:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:
            total += arrays[nx][ny]
        else:
            return -1
    return total

max_cnt = 0
for i in range(n):
    for j in range(m):
        for block in blocks:
            max_cnt = max(max_cnt, block_calculate(i, j, block))

print(max_cnt)