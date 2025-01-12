def pickingNumbers(a):
    a = sorted(a)
    temp = list(set(a))
    temp = sorted(temp)

    if len(temp) == 1:
        return n
    
    max_cnt = 0
    for i in range(len(temp)-1):
        if temp[i + 1] - temp[i] <= 1:
            cnt = a.count(temp[i]) + a.count(temp[i+1])
            if max_cnt < cnt:
                max_cnt = cnt 
        else:
            cnt = a.count(temp[i])
            if max_cnt < cnt:
                max_cnt = cnt
    
    return max_cnt

# a = [66, 66, 66, 66, 66, 66]
a = [4, 97, 5, 97, 97, 4, 97, 4, 97, 97, 97, 97, 4, 4, 5, 5, 97, 5, 97, 99, 4, 97, 5, 97, 97, 97, 5, 5, 97, 4, 5, 97, 97, 5, 97, 4, 97, 5, 4, 4, 97, 5, 5, 5, 4, 97, 97, 4, 97, 5, 4, 4, 97, 97, 97, 5, 5, 97, 4, 97, 97, 5, 4, 97, 97, 4, 97, 97, 97, 5, 4, 4, 97, 4, 4, 97, 5, 97, 97, 97, 97, 4, 97, 5, 97, 5, 4, 97, 4, 5, 97, 97, 5, 97, 5, 97, 5, 97, 97, 97]
n = len(a)

answer = pickingNumbers(a)
print(answer)

'''
temp = [4, 5, 97]
'''