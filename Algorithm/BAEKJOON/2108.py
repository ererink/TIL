n = int(input())
nums = []

for _ in range(n):
    nums.append(int(input()))

nums = sorted(nums)

average = sum(nums) / n
print(round(average))

median = nums[len(nums) // 2]
print(median)

# 최빈값
max_num = 0
mode = {}

for i in nums:
    mode[i] = mode.get(i, 0) + 1
mx = max(mode.values())


cc = []
for k, v in mode.items():
    if v == mx:
        cc.append(k)
cc.sort()

if len(cc) == 1:
    print(cc[0])
else:
    print(cc[1])

print(nums[-1] - nums[0])
