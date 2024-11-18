# 완전탐색
n = int(input())
arrays = []
for i in range(n):
    line = list(map(int, input().split()))
    arrays.append(line)
max_val = 0
for i in range(n - 2):
    for j in range(n - 2):
        val = 0
        for k in range(i, i + 3):
            for v in range(j, j + 3):
                if arrays[k][v] ==  1:
                    val += 1
        if val > max_val:
            max_val = val
print(max_val)