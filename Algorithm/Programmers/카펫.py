def solution(brown, yellow):
    answer = []
    total = brown + yellow
    
    for i in range(1, yellow + 1):
        if yellow % i == 0:
            row = max(i, yellow // i)
            col = min(i, yellow // i)
            if (row + 2) * (col + 2) == total:
                answer.append(row + 2)
                answer.append(col + 2)
                break

    return answer