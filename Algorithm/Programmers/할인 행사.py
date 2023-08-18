def solution(want, number, discount):
    answer = 0
    n = len(discount)
    want_items = []
    for i in range(len(want)):
        for j in range(number[i]):
            want_items.append(want[i])
    want_items = sorted(want_items)
    
    for i in range(n - 9):
        items = discount[i : i + 10]
        items = sorted(items)
        
        if want_items == items:
            answer += 1

    
    return answer