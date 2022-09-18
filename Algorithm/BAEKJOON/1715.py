import heapq

n = int(input())

bundle = []
for _ in range(n):  
    heapq.heappush(bundle, int(input()))

if len(bundle) == 1:
    print(0)

else:
    result = 0
    while len(bundle) > 1:
        index_0 = heapq.heappop(bundle)
        index_1 = heapq.heappop(bundle)
        result += index_0 + index_1
        heapq.heappush(bundle, index_0 + index_1)


    print(result)