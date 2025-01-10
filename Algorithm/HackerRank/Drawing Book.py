def pageCount(n, p):
    if n == p:
        return 0
    last = abs(n - p) // 2 
    first = abs(1 - p) // 2
    if p % 2 == 0:
        first += 1
    if last == 0:
        if n % 2 == 0:
            last += 1
    return min(last, first)

n = 6
p = 5

