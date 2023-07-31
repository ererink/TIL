def solution(keymap, targets):
    answer = []
    n = len(keymap)
    
    for i in targets:
        result = 0
        for j in i:
            comp = 9999
            flag = 0
            ######## target 문자 하나 출력

            for k in range(n):
                # 만약 문자열에 탐색 문자가 있다면
                if j in keymap[k]:
                    flag = 1
                    for v in range(len(keymap[k])):
                        if keymap[k][v] == j:
                            # 비교 변수에 할당
                            if (v + 1) < comp: # 기존보다 더 작은 수 할당
                                comp = (v + 1)
            if flag == 0:
                result = -1
                break
            else:
                result += comp
            
        answer.append(result)
                
    return answer