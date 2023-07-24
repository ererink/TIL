def solution(N, stages):
    answer = []
    users = len(stages)
    failure = {}
    
    # 스테이지
    for i in range(1, N+1):
        # 통과 플레이어 검사
        players = 0
        challengers = stages.count(i)
        for j in range(users):
            
            # 현재 스테이지보다 큰 수를 가지고 있는 플레이어 카운트 == 스테이지 도전 플레이어
            if i <= stages[j]:
                players += 1
                
        if challengers == 0:
            failure[i] = 0
        else:
            failure[i] = (challengers / players)
            
    # result = sorted(failure, key = lambda x : (-x[1], x[0]))
    for k, v in sorted(failure.items(), key = lambda x : (-x[1], x[0])):
        answer.append(k)
            
    return answer