# 빙고

maps = [list(map(int, input().split())) for _ in range(5)]  # 빙고판은 2차원 배열
answer = []
for _ in range(5):                                          # 사회자 답안은 1차원 배열
    answer += list(map(int, input().split()))

def search():
    bingo = 0
    # 가로 탐색
    for x in maps:
        if x.count(0) == 5:
            bingo += 1

    # 세로 탐색
    for i in range(5):
        y_chk = 0
        for j in range(5):
            if maps[j][i] == 0:
                y_chk += 1

        if y_chk == 5:
            bingo += 1

    # 왼쪽 대각선 탐색
    ld = 0
    for i in range(5):
        if maps[i][i] == 0:
            ld += 1
    if ld == 5:
        bingo += 1
    
    # 오른쪽 대각선 탐색
    rd = 0
    for i in range(5):
        if maps[i][4-i] == 0:
            rd += 1
    if rd == 5:
        bingo += 1

    return bingo

cnt = 0
for i in range(25): # 사회자 답안
    for x in range(5):  # 빙고판 탐색
        for y in range(5):
            if answer[i] == maps[x][y]:
                maps[x][y] = 0
                cnt += 1

    if cnt >= 12:           # 지운 숫자가 12개 이상이라면
        result = search()   # 빙고를 탐색하는 함수 호출

        if result >= 3:     # 빙고가 3개 이상일 경우
            print(i + 1)    # 현재 사회자의 반복문 순서인 i에 1을 더하여 출력한다.
            break
