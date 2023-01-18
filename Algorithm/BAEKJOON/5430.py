# AC
import sys

from collections import deque

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    p = input().strip()                     # 명령어
    n = int(input())                        # 배열의 개수
    nums = deque(input().strip()[1:-1].split(','))

    if n == 0:
        nums = []

    R = 0
    for i in range(len(p)):
        if p[i] == 'R':
            R += 1                  # R이 두번 있으면 뒤집을 필요가 없으므로 카운트
        
        elif p[i] == 'D':
            if len(nums) == 0:
                print('error')
                break

            else:
                if R % 2 == 0:
                    nums.popleft()
                
                else:
                    nums.pop()      # R이 홀수번 있으면 뒤집기를 해줘야 하므로 뒤집기 대신 오른쪽에서 정수를 빼준다.
            
    else:
        if R % 2 == 1:              # R이 홀수일 경우 뒤집어서 출력해주어야 한다.
            nums.reverse()
        print('[' + ",".join(nums) + ']')