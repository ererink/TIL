# 큐 2
'''
push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''
from collections import deque

n = int(input())
queue = deque(list())

for _ in range(n):
    order = input().split()

    if 'push' in order:
        queue.append(order[1])

    elif 'pop' in order:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())

    elif 'size' in order:
        print(len(queue))
    
    elif 'empty' in order:
        if not queue:
            print(1)
        else:
            print(0)
    elif 'front' in order:
        if not queue:
            print(-1)
        else:
            print(queue[0])
    
    elif 'back' in order:
        if not queue:
            print(-1)
        else:
            print(queue[-1])

