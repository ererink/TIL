import sys

t = int(input())
for test_case in range(1, t + 1):

    s = set(input())

    if len(s) == 2:
        print('#{} {}'.format(test_case, 'Yes'))
    
    else:
        print('#{} {}'.format(test_case, 'No'))
    


sys.stdin = open("_반반.txt")
