def balancedSums(arr):
    start = 0
    left_sum = 0
    right_sum = sum(arr[1:])  # 초기 오른쪽 합: 배열의 첫 번째 값을 제외한 전체 합

    # 한 번 순회하며 왼쪽 합과 오른쪽 합 비교
    while start < len(arr):
        if left_sum == right_sum:
            return "YES"
        
        # 오른쪽 합에서 다음 값을 제거
        if start + 1 < len(arr):
            right_sum -= arr[start + 1]
        
        # 왼쪽 합에 현재 값을 추가
        left_sum += arr[start]
        
        # 다음 인덱스로 이동
        start += 1

    return "NO"
