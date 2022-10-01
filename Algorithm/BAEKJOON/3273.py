# 두수의 합

from curses import start_color


n = int(input())
nums = list(map(int, input().split()))
x = int(input())

nums = sorted(nums)
i = 0
j = n - 1
cnt = 0

while i < j:
    # 더한 값이 x보다 작으면 start를 오른쪽으로 이동
    if  nums[i] + nums[j] < x:
        i += 1
    # 더한 값이 x보다 크면 end를 왼쪽으로 이동
    elif nums[i] + nums[j] > x:
        j -= 1
    
    # 더한 값이 x와 같으면 카운트
    else:
        cnt += 1
        i += 1
        j -= 1

print(cnt)
        

    
