# 그리디 알고리즘
def solution(n, m, section):
    answer = 0
    arrays = [1] * n
    for i in section:
        arrays[i-1] = 0

    for i in range(n - m + 1):
        if arrays[i] == 0:
            for j in range(i, i + m):
                arrays[j] = 1
            answer += 1

    if 0  in arrays:
        answer += 1
                
    return answer