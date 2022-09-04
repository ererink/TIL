t = int(input())
for _ in range(t):
    ox_list = list(input())
    score = 0
    check =[]

    for i in ox_list:
        check.append(i)
        if 'O' in i:
            score += 1
            if len(check) > 1:
                score += (len(check) - 1)
        
        else:
            check.clear()
    print(score)
        
