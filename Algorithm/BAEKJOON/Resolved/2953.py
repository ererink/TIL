total = []

for order in range(5):
    score = map(int, input().split())
    result = 0
    for i in score:
        result += i
    total.append(result)
    
print(total.index(max(total)) + 1, max(total))