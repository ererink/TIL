def solution(x):
    answer = [0, 0]

    while True:
        if x == '1':
            break
            
        answer[1] += x.count('0')
        x = x.replace('0', '')
        length = len(x)
        x = bin(length)[2:]
        answer[0] += 1
    
    return answer