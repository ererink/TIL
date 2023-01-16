# 카드2

from collections import deque

n = int(input())

cards = deque()
for i in range(1, n + 1):
        cards.append(i)
        
while len(cards) != 1:
    cards.popleft()
    cards.append(cards.popleft())

print(*cards)