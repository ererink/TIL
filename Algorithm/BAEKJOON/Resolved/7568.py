n = int(input())
bulk = []

for _ in range(n):
    x, y = map(int, input().split())
    bulk.append([x, y])

if 1:
    
    bulk[0] = n
else:
    bulk[1:-2] = 2
print(bulk)