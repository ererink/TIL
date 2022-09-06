n = int(input())
hills = list(map(int, input().split()))
check = []
hill = []

for i in range(n-1):
    if hills[i + 1] > hills[i]:
        check.append(hills[i])
        check.append(hills[i + 1])
        hill.append((max(check) - min(check)))

        
    elif hills[i + 1] <= hills[i]:
        check.clear()
        continue
    

if len(check) == 0:
    hill.append(0)
print(max(hill))