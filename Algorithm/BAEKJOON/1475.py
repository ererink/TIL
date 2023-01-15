# 방번호

room = input()
nums = [0] * 10

for i in range(len(room)):
    n = int(room[i])

    # 6와 9 중 더 작은 값을 가지는 인덱스가 +1을 한다
    if n == 6 or n == 9:
        if nums[6] <= nums[9]:
            nums[6] += 1
        else:
            nums[9] += 1
    # 6과 9의 값이 아닌 경우 인덱스 값을 +1 해준다 
    else:
        nums[n] += 1

print(max(nums))