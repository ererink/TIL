# 시도한 코드
def solution(cap, n, deliveries, pickups):
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]
    answer = 0
    d_chk = 0
    p_chk = 0
    flag = 0
    
    for i in range(n):
        if cap >= d_chk + deliveries[i]:
            d_chk += deliveries[i]

        else:
            answer += i + (n - i)
            d_chk = deliveries[i]
            flag = i
            
        if i == (n-1):
            answer += (n - flag)

        
    return answer * 2


# 답안 코드
def solution(cap, n, deliveries, pickups):
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]
    answer = 0
    d_chk = 0
    p_chk = 0

    for i in range(n):
        d_chk += deliveries[i]
        p_chk += pickups[i]

        while d_chk > 0 or p_chk > 0:
            d_chk -= cap
            p_chk -= cap
            answer += (n - i) * 2

    return answer