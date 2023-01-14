# 방번호

room = input()
nums = [0] * 10

for i in range(len(room)):
    n = int(room[i])
    if n == 6 or n == 9:
        if nums[6] <= nums[9]:
            nums[6] += 1
        else:
            nums[9] += 1
    else:
        nums[n] += 1

print(max(nums))