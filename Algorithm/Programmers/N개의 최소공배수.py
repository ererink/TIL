def solution(arr):
    answer = 0
    chk = 0
    gcd = 0
    for i in arr:
        if chk == 0:
            chk = i
        else:
            if chk < i:
                a = i; b = chk
            else:
                a = chk; b = i
            c = a % b
            if c == 0:
                gcd = b
            else:
                while c != 0:
                    c = a % b
                    if c != 0:
                        a = b; b = c  
                    else:
                        gcd = b
                        break
        if gcd != 0:                
            lcm = (chk * i) // gcd
            chk = lcm
    answer = chk
    return answer