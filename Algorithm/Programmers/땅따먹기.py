# DP문제
def solution(land):
    n = len(land)
    for i in range(1, n): # 이전 행 탐색
        for j in range(4): 
            # 최대값 갱신
            land[i][j] += max(land[i-1][0:j] + land[i-1][j+1:])
    return max(land[-1])
