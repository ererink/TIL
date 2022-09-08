taebo = input()
punch = [0, 0]
l = 0
for i in taebo:
    if i == '@':
        punch[l] += 1
    
    elif i == '(':
        l += 1

print(*punch)
    

