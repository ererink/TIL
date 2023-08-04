def solution(n):
    answer = 0
    s = bin(n)[2:]
    cnt = s.count('1')
    new_n = n + 1
    
    while True:
        if bin(new_n)[2:].count('1') == cnt:
            answer = new_n
            return answer
            break
        else:
            new_n += 1
            
    return answer