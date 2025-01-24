def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_cnt = 0
    orange_cnt = 0
    for i in range(m):
        if (a + apples[i]) >= s and (a + apples[i]) <= t:
            apple_cnt += 1
    
    for j in range(n):
        if (b + oranges[j]) >= s and (b + oranges[j]) <= t:
            orange_cnt += 1 
    
    print(apple_cnt)
    print(orange_cnt)

s = 7
t = 11
a = 5
b = 15
m = 3
n = 2
apples = [-2, 2, 1]
oranges = [5, -6]

# print(countApplesAndOranges(s, t, a, b, apples, oranges))
countApplesAndOranges(s, t, a, b, apples, oranges)