def solution(babbling):
    answer = 0
    nephew = ["aya", "ye", "woo", "ma" ]
    for i in babbling:
        chk = ''
        result = ''
        prev = ''
        for j in i:
            chk += j
            if chk in nephew:
                if prev != chk:
                    result += chk
                    prev = chk
                    chk = ''

        if result == i:
            answer += 1
            
    return answer