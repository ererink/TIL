def solution(n, lost, reserve):
    answer = 0
    lost = sorted(lost)
    reserve = sorted(reserve)

    # 여별을 가지고 있는 학생이 잃어버릴 경우 탐색
    idx = 0
    for i in range(len(lost)):
        if lost[idx] in reserve:
            x = lost[idx]
            lost.remove(x)
            reserve.remove(x)
        else:
            idx += 1

        if len(lost) <= idx:
            break
            
    for i in reserve:
        if lost:
            if i - 1 in lost:
                lost.remove(i - 1)
            elif i + 1 in lost:
                lost.remove(i + 1)
    
    for i in range(1, n + 1):
        if i in lost:
            continue
        else:
            answer += 1
    
    return answer