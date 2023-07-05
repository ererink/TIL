def solution(numbers):
    answer = []
    n = len(numbers)
    
    for i in range(n - 1):
        cal = 0
        for j in range(i + 1, n):
            answer.append(numbers[i] + numbers[j])
            
    answer = set(answer)
    answer = sorted(answer)
    return answer