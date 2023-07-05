def solution(food):
    answer = ''
    n = len(food)
    cnt = []
    cnt.append(0)
    
    for i in range(1, n):
        sep = food[i] // 2
        # print(sep)
        cnt.append(sep)
    
    # 음식 개수만큼 할당
    for i in range(1, len(cnt)):
        for j in range(cnt[i]):
            answer += str(i)
    answer += '0'
    
    for i in range(len(cnt)-1, 0 , - 1):
        for j in range(cnt[i]):
            answer += str(i)
            
    return answer