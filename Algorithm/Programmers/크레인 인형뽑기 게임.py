from collections import deque

def solution(board, moves):

    N = len(board)
    col_b = []

    # 열 배열 생성
    for i in range(N):
        line = []
        for j in range(N-1, -1, -1):
            if board[j][i] != 0:
                line.append(board[j][i])
        col_b.append(line)

    picked = []
    check = 0
    cnt = 0

    for i in range(len(moves)):
        if not col_b or not col_b[moves[i]-1]:  # col_b에 값이 없을 때 예외처리
            continue
        check = col_b[moves[i] - 1].pop()
        if not picked:                          # picked에 값이 없을 때 값 추가
            picked.append(check)
        elif check == picked[-1]:               
            picked.pop()
            cnt += 2
        else:
            picked.append(check)

    return cnt