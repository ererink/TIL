# 리스트에서 두개의 정수를 더하여 Target과 같은 합의 인덱스를 반환한다.

def twoSum(self, nums: List[int], target: int) -> List[int]:
    answer = []
    for i in range(len(nums)):
        check = nums[i]
        for j in range(i + 1, len(nums)):
            check += nums[j]
            if check == target:
                answer.append(i)
                answer.append(j)
                break
            else:
                check = nums[i]
    return answer

# 다른 답안
def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] == target - nums[i]:
                return [i, j]
    # Return an empty list if no solution is found
    return []