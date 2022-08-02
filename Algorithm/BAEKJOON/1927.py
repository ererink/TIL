# 최소 힙
# 배열에 자연수 x를 넣는다.
# 배열에서 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.
# 첫째 줄에 연산의 개수, 다음 N개의 줄에는 연산에 대한 정보이다. 
# x가 자연수라면 배열에 x라는 값을 넣는(추가하는) 연산이고, -> heappush
# x가 0이라면 배열에서 가장 작은 값을 출력하고 그 값을 배열에서 제거하는 경우이다. -> heqapq.heappop

# 0이면 제거, 자연수면 추가 

#  0이 주어진 횟수만큼 답을 출력한다.
#  만약 배열이 비어 있는 경우, 0을 출력하면 된다.

import heapq
t = int(input())
for test_case in range(t):

    numbers = int(input())
    heap = []
    # .heapify를 생략해도 가능하다

    for number in numbers:
        if number != 0:                         # 0이 아니면 추가한다.
            heapq.heappush(heap, number) 
        else:
            if len(heap):                       # 비어있는 경우를 , 'length가 있으면/없으면', 'len(heap) == 0'은 참이니까. 
                print(0)
            else:
                print(heapq.heappop(heap))      # 0이면 제거한다. 
