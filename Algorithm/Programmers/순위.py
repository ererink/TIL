def solution(n, results):
    answer = 0
    win = [[] for _ in range(n + 1)]
    lose = [[] for _ in range(n + 1)]
    visited = [[] * n for _ in range(n)]
    rank = [] * (n+1)
    
    for a, b in results:
        win[a].append(b)                    # a 선수에게 패배를 당한 b 선수들 번호 할당
        lose[b].append(a)                   # b 선수가 패배를 당한 a 선수들 할당   
    
    for i in range(1, n+1):                 # i는 현재 탐색하는 선수
        for j in win[i]:                    # i를 상대로 패배한 선수들 j에 할당
            if lose[i]:                     # 진 기록이 있는 경우
                for k in lose[i]:           # 현재 탐색 선수의 패배 기록 탐색 (현재 선수를 상대로 이긴 선수 == k)
                    if k not in lose[j]:    # i를 상대로 패배한 선수(j)의 패배기록에 현재 탐색 선수를 상대로 이긴 선수의 번호가 없다면
                        lose[j].append(k)   # i를 상대로 패배한 선수(j)의 패배기록에 기록 (j는 이미 현재 탐색 선수(i)에게 패배했으므로 현재 탐색 선수(i)를 상대로 이긴 선수(k)에게 패배하게 된다)
                    if j not in win[k]:
                        win[k].append(j)
                        
    
    for i in range(1, n + 1):
        # 모든 경기 결과가 있는 경우 순위 기록이 가능하다. 모든 경기 결과의 수는 (총 선수들의 수 - 1)
        if len(win[i]) + len(lose[i]) == (n - 1): 
            answer += 1 
            
    return answer

