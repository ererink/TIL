# 숫자 카드 2
'''
input = 
10                          -> 숫자 카드 개수
6 3 2 10 10 10 -10 -10 7 3  -> 숫자 카드
8                           -> 찾아야 하는 숫자 개수
10 9 -5 2 3 4 5 -10         -> 찾아야 하는 숫자 나열
'''


N = int(input())
cards = list(input().split())
M = int(input())
targets = list((input().split()))
result = {}

for i in cards:                         # else 이외에 i에 해당하는 값이 더 있다면 1을 더해준다.
    if i in result:
        result[i] += 1
    
    else:
        result[i] = 1                   # 일단 cards에 해당하는 값을 1 값을 넣어준다. 

for j in targets:                       
    if j in result:                     # targets에 해당하는 값이 딕셔너리에 있다면 
        print(result[j], end=" ")       # 해당 값을 출력하고
    
    else:
        print(0, end=" ")               # 없다면 0을 출력한다.
