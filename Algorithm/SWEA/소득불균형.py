T = int(input())
for test_case in range(1, T + 1):
    
    t = int(input())
    nums_input = list(map(int, input().split()))

    sum_ = 0
    avg_ = 0

    for i in range(t):
        sum_ += nums_input[i] # plus
    
    avg = sum_ / len(nums_input) #avg

    low_income = 0
    for j in range(t):
        if nums_input[j] <= avg: #count low avg
            low_income += 1
        
    print('#{} {}'.format(test_case, low_income))