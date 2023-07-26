def solution(dartResult):
    answer = 0
    prev = 0; now = 0 ; temp = ''

    for i in dartResult:
       # 두자리 수 고려
        if i == 'S':
            prev = now
            now = int(temp)
            temp = ''
            continue

        elif i == 'D':
            prev = now
            now  = int(temp)
            temp = ''
            now **= 2

        elif i == 'T':
            prev = now
            now = int(temp)
            temp = ''
            now **= 3

        elif i == '*':
            prev *= 2
            now *= 2
            answer += prev
            prev = 0

        elif i == '#':
            now *= -1
            answer += prev
            prev = 0
        else:
            temp += i
            if prev != 0:
                answer += prev
                prev = 0

    answer += prev
    answer += now

    return(answer)