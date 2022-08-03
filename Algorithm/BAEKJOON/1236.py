# 성 지키기

# try 1
from pprint import pprint

n, m = map(int, input().split())
matrix = []
cnt = 0
result = 0
for _ in range(n):
    line = list(input())
    matrix.append(line)
 
for i in range(n):
    result += cnt
    cnt += 1
    for j in range(m):
        
        if 'X' in matrix[i][j]:
            cnt = 0
            result -= 1
        else:
            continue

pprint(result)

# matrix = [list(map(int, input().split())) for _ in range(m)] 

# answer
n, m = map(int, input().split())
matrix = []
row_cnt = 0
col_cnt = 0

for _ in range(n):
    line = list(input())
    matrix.append(line)

for i in range(n):
    if 'X' not in matrix[i] :
        row_cnt += 1

for j in range(m):
    if "X" not in [matrix[i][j] for i in range(n)]:        
        col_cnt += 1

print(max(row_cnt, col_cnt))
#  X가 들어있지 않는 행, 열의 개수를 구하고 그 중 큰 값을 출력