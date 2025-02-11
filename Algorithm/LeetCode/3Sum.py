def threeSum(nums):
    nums = sorted(nums)     # 배열을 정렬하여 같은 값이 인접하도록 하여 불필요한 과정을 줄인다.
    n = len(nums)           
    answer = []

    for i in range(n):      # (n - 2)를 해줘도 됨
        if i > 0 and nums[i] == nums[i-1]:  # 첫번째 값이 다음으로 이동할 때 이전 값과 같다면 같은 결과가 도출하므로 건너뛴다. (중복 제거)
            continue 

        left = i + 1    # 두번째 값, 첫번째 포인터
        right = n - 1   # 세번째 값, 두번째 포인터

        while left < right:
            check = nums[i] + nums[left] + nums[right]  # 세값의 총합

            if check == 0:
                line = [nums[i], nums[left], nums[right]]
                answer.append(line)                     # 0일 경우 정답

                while left < right and nums[left] == nums[left + 1]:    # 포인터 이동 시 같은 값이라면 같은 결과를 도출하므로 건너뛰기
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                    
                left += 1
                right -= 1

            elif check < 0:     # 총합이 음수라면 값을 양수쪽으로 이동할 수 있도록 왼쪽 포인터가 이동
                left += 1
            else:               # 총합이 양수라면 값을 음수 쪽으로 이동할 수 있도록 오른쪽 포인터가 이동
                right -= 1
    
    return answer

nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))


# 다른 답변
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n - 2):
            # 첫번째 값이 0보다 클 경우 이후 2개 정수 값도 양수이므로 0이 만들어질 수 없음
            if nums[i] > 0:
                break
            if i and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, n - 1
            while j < k:
                x = nums[i] + nums[j] + nums[k]
                if x < 0:
                    j += 1
                elif x > 0:
                    k -= 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    j, k = j + 1, k - 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
        return ans