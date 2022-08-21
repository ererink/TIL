# 세로읽기
matrix = [[0] * 15 for _ in range(5)]


for i in range(5):
    line = list(input())
    for j in range(len(line)):
        matrix[i][j] = line[j]

# 열 탐색
for i in range(15):
    for j in range(5):
        if matrix[j][i] == 0:
            continue

        else:
            print(matrix[j][i], end='')
        