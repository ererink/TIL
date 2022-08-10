n, m = map(int, input().split())

x1 = (n-1) // 4 + 1
y1 = (n-1) % 4
x2 = (m-1) // 4 + 1
y2 = (m-1) % 4

answer = (abs(x2 - x1) + abs(y2 -y1))

print(answer)