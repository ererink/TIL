def threeSum(nums):
    nums = sorted(nums)
    n = len(nums)
    answer = []

    for i in range(n):
        if i > 0 and nums[i] == nums[i-1]:
            continue 

        left = i + 1
        right = n - 1

        while left < right:
            check = nums[i] + nums[left] + nums[right]

            if check == 0:
                line = [nums[i], nums[left], nums[right]]
                
                answer.append(line)

                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                    
                left += 1
                right -= 1

            elif check < 0:
                left += 1
            else:
                right -= 1
    
    return answer

nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))
