def miniMaxSum(arr):
    arr = sorted(arr)
    min_sum = 999999999999999
    max_sum = 0
    
    for i in range(2):
        check = 0
        for j in range(i, i + 4):
            check += arr[j]
        print(check)
        if check < min_sum:
            min_sum = check
        
        elif check > max_sum:
            max_sum = check
            
    print(min_sum, max_sum)

arr = [256741038, 623958417, 467905213, 714532089, 938071625]
answer = miniMaxSum(arr)