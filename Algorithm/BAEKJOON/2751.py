# sort()

n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))
    
b = sorted(a)

for i in b:
    print(i)