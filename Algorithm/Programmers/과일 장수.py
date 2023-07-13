from collections import deque
def solution(k, m, score):
    answer = 0
    score = sorted(score, reverse=True)
    score = deque(score)
    
    def fruit():
        nonlocal answer
        nonlocal score
        profit = []
        for i in range(m):
            profit.append(score.popleft())
            
        answer += (min(profit) * m)
        

    while len(score) >= m:
        fruit()
    
    return answer