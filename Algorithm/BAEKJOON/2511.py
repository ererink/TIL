# 카드놀이

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_cnt = 0
B_cnt = 0

last_win = 0

for i in range(10):
    if A[i] > B[i]:
        A_cnt += 3
        last_win = 1
    elif A[i] < B[i]:
        B_cnt += 3
        last_win = -1
    else:
        A_cnt += 1
        B_cnt += 1
        

print(A_cnt, B_cnt)

if A_cnt > B_cnt:
    print('A')

elif A_cnt < B_cnt:
    print('B')

else:
    if last_win == 1:
        print('A')
    elif last_win == -1:
        print('B')
    else: 
        print('D')
