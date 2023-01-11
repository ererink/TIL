# 용액 

n = int(input())
nums = list(map(int, input().split()))

left, right = 0, n - 1                      # 왼쪽 인덱스와 오른쪽 인덱스 위치 값
diff = abs(nums[left] + nums[right])        # 왼쪽 인덱스와 오른쪽 인덱스 빼준 값을 담아주는 변수
l = nums[left]                              # 계산된 인덱스 값을 각자 할당해준다
r = nums[right]

while left < right:                         # 왼쪽 인덱스 위치가 오른쪽 인덱스 위치를 넘지 않을 때 까지
    check = nums[left] + nums[right]        # 왼쪽 인덱스와 오른쪽 인덱스 빼준 값 할당
    
    if abs(check) < diff:                   # 만약 다른 조합으로 빼준 값이 기존 빼준 값보다 작으면
        diff = abs(check)                   # 새로운 값을 할당한다. 이는 0에 가까운 수가 된다.
        l = nums[left]
        r = nums[right]
        
    if check < 0:                           # 빼준 값이 0보다 작으면
        left += 1                           # 왼쪽 인덱스는 오른쪽으로 한칸 이동
    
    else:                                   # 빼준 값이 0보다 크면
        right -= 1                          # 오른쪽 인덱스는 왼쪽으로 한칸 이동
        
print(l, r)