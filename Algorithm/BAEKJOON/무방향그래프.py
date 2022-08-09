'''
input = 
6 5
1 2
2 5
5 1
3 4
4 6

output = [
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 1, 0, 0, 1, 0],
 [0, 1, 0, 0, 0, 1, 0],
 [0, 0, 0, 0, 1, 0, 0],
 [0, 0, 0, 1, 0, 0, 1],
 [0, 1, 1, 0, 0, 0, 0],
 [0, 0, 0, 0, 1, 0, 0]]
[[], [2, 5], [1, 5], [4], [3, 6], [2, 1], [4]]

n = 정점 개수
m = 간선 개수
'''
import pprint

n, m = map(int, input().split())
adjacent = []

graph = [[0] * (n+1) for _ in range(n+1)]
graph_list =  [[] for _ in range(n+1)]

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1][v2] = 1
    graph[v2][v1] = 1
    graph_list[v1].append(v2)
    graph_list[v2].append(v1)

pprint.pprint(graph)
print(graph_list)