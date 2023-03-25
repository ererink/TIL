import math
def solution(n, words):
    answer = []
    check = []
    w_len = len(words)
    for i in range(w_len):
        if len(check) > 0:
            w = words[i]
            c = check[-1]
            if w in check:
                if ((i+1) % n) == 0:
                    answer.append(n)
                    answer.append(math.ceil((i+1)/n))
                    return answer
                else:
                    answer.append((i+1) % n)
                    answer.append(math.ceil((i+1)/n))
                    return answer
                    
            if c[-1] != w[0]:
                if ((i+1) % n) == 0:
                    answer.append(n)
                    answer.append(math.ceil((i+1)/n))
                    return answer
                else:
                    answer.append((i+1) % n)
                    answer.append(math.ceil((i+1)/n))
                    return answer
            check.append(words[i])
        else:
            check.append(words[i])
    
    if len(answer) == 0:
        answer.append(0)
        answer.append(0)
    return answer