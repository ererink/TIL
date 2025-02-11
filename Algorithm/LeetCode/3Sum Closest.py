def threeSumClosest(nums, target):
    nums = sorted(nums)
    n = len(nums)
    answer = 0
    min_diff = float('inf')
    
    for i in range(n - 2):
        total = 0
        left, right = i + 1, n - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]
            diff = abs(total - target)
            print(i, left, right, "|", "total :", total, "diff :", diff)

            if diff < min_diff:
                min_diff = diff
                answer = total

            if total == target:
                return total
                
            elif total < target:
                left += 1
            else:
                right -= 1

    return answer

nums = [4,0,5,-5,3,3,0,-4,-5]
target = -2
print(threeSumClosest(nums, target))