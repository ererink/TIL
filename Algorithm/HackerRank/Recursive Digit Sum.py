def superDigit(n, k):
    superD = 0
    for i in n:
        superD += int(i)
    superD *= k 

    while len(str(superD)) > 1:
        temp = 0
        for i in str(superD):
            temp += int(i) 
        superD = temp 
    
    return superD