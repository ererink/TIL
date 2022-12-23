# 대표값2
# 다섯 개의 자연수가 주어질 때 이들의 평균과 중앙값을 구하는 프로그램을 작성하시오.

nums = []
for _ in range(5):
    nums.append(input())

average = 0
for i in nums:
    average += int(i)

medium = sorted(nums)[2]


print(average // 5)
print(medium)