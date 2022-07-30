# X보다 작은 수

A, X = map(int, input().split())
nums = list(map(int, input().split()))


for i in range(A):
    if X > nums[i]:
        print(nums[i], end=" ")