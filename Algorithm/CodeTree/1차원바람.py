from collections import deque

n, m, q = map(int, input().split())
arrays = []
for i in range(n):
    line = deque(map(int, input().split()))
    arrays.append(line)

# 행 이동 함수
def wind_row(row, d):
    if d == 'L':
        temp = arrays[row].pop()
        arrays[row].appendleft(temp)
        return 'R'  
    else:
        temp = arrays[row].popleft()
        arrays[row].append(temp)
        return 'L' 


# 전파 조건 확인 함수
def check_column(from_row, to_row):
    for j in range(m):
        if arrays[from_row][j] == arrays[to_row][j]:
            return True
    return False


# 바람 처리
for _ in range(q):
    r, d = input().split()
    r = int(r) - 1
    origin_d = d

    d = wind_row(r, d)

    # r보다 위 탐색
    for i in range(r - 1, -1, -1):
        if not check_column(i + 1, i):  # 위쪽 전파 가능 확인
            break
        d = wind_row(i, d)

    # 방향 바꾸기 
    if origin_d == "R":
        d = "L"
    else:
        d = "R"

    # r보다 아래 탐색
    for i in range(r + 1, n):
        if not check_column(i - 1, i):  # 아래쪽 전파 가능 확인
            break
        d = wind_row(i, d)

# 결과 출력
for row in arrays:
    print(" ".join(map(str, row)))
