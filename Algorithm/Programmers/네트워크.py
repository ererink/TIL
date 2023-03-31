from collections import deque
def solution(n, computers):
    answer = 0
    network = [[] * n for _ in range(n)]
    visited = [False] * n 
    
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                network[i].append(j)
                network[j].append(i)
                
    for i in range(n):
        if not visited[i]:
            search(i, visited, network)
            answer += 1
    return answer

def search(start, visited, network):
    queue = deque()
    queue.append(start)
    visited[start] = True
    
    while queue:
        x = queue.popleft()
        
        for i in network[x]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
    

