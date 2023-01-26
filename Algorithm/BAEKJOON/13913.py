# 숨바꼭질4

from collections import deque

n, k = map(int, input().split())
MAX = 100001

visited = [-1] * (MAX)
visited[n] = 0

queue = deque()
queue.append((n, [n]))

# 수진이가 동생보다 더 큰 위치에 있을 때
if n > k:
    print(n - k)

    for i in range(n, k - 1, -1):
        print(i, end=' ')

else:

    while queue:
        x, path = queue.popleft()

        # 동생에게 도착
        if x == k:
            print(visited[x])
            print(*path)
            break

        for j in (x - 1, x + 1, x * 2):
            if 0 <= j < MAX and visited[j] == -1:
                visited[j] = visited[x] + 1
                queue.append((j, path + [j]))
