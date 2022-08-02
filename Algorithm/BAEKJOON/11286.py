# 절대값 힙
# 시간초과

import heapq

N = int(input())
heap = []

for test_case in range(N):
    numbers = int(input())

    # 입력값이 0이 아닌 경우
    if numbers != 0:                                    # 0이 아니면 heap 리스트에 입력값을 추가한다.
        heapq.heappush(heap, (abs(numbers), numbers))   # 절대값과 원래값을 같이 저장한다. (1, -1)
                                                        # 리스트에는 하나의 인덱스에 두개의 값이 있는 "튜플"을 저장한다.
                                                        # 절대값이 기준이지만 제일 작은 수가 여러개일 때 원래 값을 기준으로 작은 값을 탐색한다.
                                                        
    # 입력값이 0인 경우
    else:
        if len(heap) == 0:                              # heappop으로 리스트의 값을 다 뺀 경우
            print(0)                                    # 0을 출력한다. (마지막 출력값이 된다)
        else:                                           # heap 리스트에 값이 있는 경우
            print(heapq.heappop(heap)[1])               # heap에서 제일 앞에 있는 (제일 작은 값)이 리스트에서 제거되고 출력된다. 
                                                        # 튜플의 인덱스 1에 위치하는 값을 출력한다.  
                                                        

   
