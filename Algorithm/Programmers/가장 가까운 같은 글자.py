def solution(s):
    answer = []
    n = len(s)
    
    # 현재 탐색하고자 하는 문자
    for i in range(n):
        gap = 999
        noword = 0
        # 현재 탐색 문자보다 앞에 있는 같은 문자 탐색
        for j in range(i):
            # 만약 앞의 문자와 같다면
            if s[i] == s[j]:
                # 더 작은 차이의 칸 할당
                if gap > (i - j):
                    gap = (i - j)
                else:
                    continue
                
            else:
                noword = -1
                
        if i == 0:
            noword = -1
            
        if gap != 999:
            answer.append(gap)
        else:
            answer.append(noword)
        
    return answer