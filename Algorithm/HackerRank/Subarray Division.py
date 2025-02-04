def birthday(s, d, m):
    answer = 0
    if len(s) == 1 and m == 1:
        return 1 
    
    for i in range((len(s) - m) + 1):
        check = 0
        for j in range(i, i + m):
            check += s[j]
            
        if check == d:
            answer += 1
    return answer

s = [2, 5, 1, 3, 4, 4, 3, 5, 1, 1, 2, 1, 4, 1, 3, 3, 4, 2, 1]
d, m = 18, 7
print(birthday(s, d, m))