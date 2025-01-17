def diagonalDifference(arr):
    left_right = 0
    right_left = 0
    
    left = 0
    right = n - 1
    for i in range(n):
        right_left += arr[left][right]
        left += 1
        right -= 1
        for j in range(n):
            if i == j:
                left_right += arr[i][j]
            
    return abs(left_right - right_left)

n = 3
arr = [
    [11, 2, 4],
    [4, 5, 6],
    [10, 8, -12]
]