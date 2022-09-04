A, B = list(input().split())
back_A = ''
back_B = ''

back_A = A[::-1]
back_B = B[::-1]

if back_A > back_B:
    print(back_A)
else:
    print(back_B)