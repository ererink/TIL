# 치팅
def solution(n, m, section):
    answer = 0
    current = 0  # 현재 덧칠하고 있는 지점

    for i in section:
        if i > current and i <= current + m:  # 해당 섹션을 덧칠할 수 있는 경우
            current = i + m - 1  # 섹션의 끝점으로 이동
            answer += 1
    return answer
