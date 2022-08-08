# 블랙잭 

n, m = map(int,input().split())                     
cards = list(map(int,input().split()))              # 카드의 값을 리스트로 받는다.
max_total = 0                                       # m에 가까운 최대치 값을 저장하기 위한 변수

for i in range(n - 2):                              
    for j in range(i + 1, n -1):
        for k in range(j + 1, n):
            total = cards[i] + cards[j] + cards[k]
            
            if max_total < total <= m:              # 합산값이 이전 최대치보다 크거나 m(목표치)에 가까운 값이라면 
                max_total = total                   # 최대치 값이 된다.
                
            if total == m:                          # m(목표치)와 같다면
                max_total = total                   # 최대치로 저장한다.
                break

print(max_total)