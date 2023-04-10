from itertools import permutations

def solution(k, dungeons):
    answer = []
    n = len(dungeons)
    temp = [] 
    
    for i in permutations(dungeons, n):
        temp.append(i)
        
    m = len(temp)
    cnt = 0
    
    for i in range(m):
        answer.append(cnt)
        check = k
        cnt = 0
        for j in range(n):
            if check >= temp[i][j][0]:
                check -= temp[i][j][1]
                cnt += 1
            else:
                break
            
    return max(answer)


    