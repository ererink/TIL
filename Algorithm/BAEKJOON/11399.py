# ATM
# 오름차순으로 정렬

n = int(input())

line = []
line = list(map(int, input().split()))
line = sorted(line)

a = 0
total = 0
for i in line:
    a += i
    total += a

print(total)