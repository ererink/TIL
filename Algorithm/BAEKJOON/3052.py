# 나머지

nums =[]                        # 입력값 저장 공간

for test_case in range(10):     # 입력 10번
    nums.append(int(input()))   # 입력한 값을 nums에 넣어준다. (정수로 변환)

result = []                     # 계산한 값 저장 공간
for i in nums: # i는 int        # 입력값을 i에 하나씩 넣어주며 반복한다
    result.append(i % 42)       # i(입력값)을 42와 나눈 나머지 값을 result에 넣어준다

print(len(set(result)))         # 중복을 제거하여 서로 다른 값의 원소 개수를 출력한다. 