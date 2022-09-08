A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_result = 0
B_result = 0

last_win = 0

for i in range(10):
    if A[i] > B[i]:
        A_result += 3
        last_win = 1
    
    elif A[i] < B[i]:
        B_result += 3
        last_win = -1
    else:
        A_result += 1
        B_result += 1

print(A_result, B_result)
if A_result > B_result:
    print('A')
elif A_result < B_result:
    print('B')

else:
    if last_win == 1:
        print('A')
    elif last_win == -1:
        print('B')
    else:
        print('D')

