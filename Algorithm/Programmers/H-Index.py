def solution(citations):
    answer = 0
    max_cnt = 0
    min_cnt = 0
    m = max(citations)
    
    if m == 0:
        return 0
    
    citations = sorted(citations)
    # 최소 인용 횟수 (주체)
    for i in range(1, m + 1):
        for j in citations:
            if i < j:
                max_cnt += 1 # 논문 개수
            else:
                min_cnt += 1
            
        if max_cnt <= i:
            if min_cnt <= i:
                return i
        else:
            max_cnt = 0
            min_cnt = 0

    