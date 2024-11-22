# 완전 탐색
n, m = map(int, input().split())
arrays = []
for _ in range(n):
    line = list(input().split())
    arrays.append(line)

if m == 1:
    print(2 * n)
    exit()
    
cnt = 0
# 가로 찾기
for i in range(n):
    temp_cnt = 1
    max_cnt = 1
    for j in range(1, n):
        if arrays[i][j] == arrays[i][j-1]:
            temp_cnt += 1
            print(temp_cnt, max_cnt)
            max_cnt = max(max_cnt, temp_cnt)
            print(max_cnt)
        else:
            temp_cnt = 1
    if max_cnt >= m:
        cnt += 1

# 세로 찾기
for i in range(n):
    temp_cnt_h = 1
    max_cnt_h = 1
    for j in range(1, n):
        if arrays[j][i] == arrays[j-1][i]:
            temp_cnt_h += 1
            max_cnt_h = max(max_cnt_h, temp_cnt_h)
        else:
            temp_cnt_h = 1
    if max_cnt_h >= m:
        cnt += 1

print(cnt)