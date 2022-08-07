import sys
from collections import deque

for _ in range(10):
    # 입력
    test_case = int(input())
    pw = deque(map(int, input().split()))

    while pw[-1] > 0:
        for i in range(1, 6):
            pw[0] = pw[0] - i
            pw.append(pw.popleft())
            if pw[-1] <= 0:
                pw[-1] = 0
                break
            
    print(f'#{test_case}', *pw)

sys.stdin = open("_암호생성기.txt")
