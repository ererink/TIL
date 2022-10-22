def solution(price, money, count):
    answer = 0
    check = 0

    for i in range(1, count + 1):
        check += price * i 
    
    if check - money > 0:
        answer = check - money
    else:
        answer = 0
    
    
    return answer