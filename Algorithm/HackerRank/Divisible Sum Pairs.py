def divisibleSumPairs(n, k, ar):
    cnt = 0
    
    for i in range(n):
        check = ar[i]
        for j in range(i + 1, n):
            check += ar[j]
            if check % k == 0:
                cnt += 1
                check = ar[i]
            else:
                check = ar[i]
    return cnt