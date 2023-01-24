from collections import deque

n, k = map(int, input().split())
nums = deque()

for i in range(1, n + 1):
    nums.append(i)

print('<', end='')                  # 요세푸스 순열 출력 전에 먼저 괄호 출력

while nums:                         # nums가 비어질 때 까지 반복
    for j in range(k - 1):          # k번째 전까지 왼쪽 숫자들을 다시 오른쪽으로 넣어서 k번째 정수들을 출력하기 위해 k-1번만 반복
        nums.append(nums[0])        # 맨 앞에 있는 정수를 뒤로 보내주는 작업
        nums.popleft()              # 무한으로 연속해서 순열을 반복할 수 있도록
    print(nums.popleft(), end='')   # k번째 출력

    if nums:                        # nums가 비어있지 않다면 (앞으로 반복할 정수들이 존재한다면)
        print(', ', end='')         # 콤마 뒤 스페이스 주의    

print('>')