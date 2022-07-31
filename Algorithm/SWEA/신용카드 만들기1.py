T = int(input())
for test_case in range(1, T + 1):

    card_nums = input().split()

    odd_result = 0
    even_result = 0

    for i in range(1, 16):
        if i % 2 == 1:
            odd_result += int(card_nums[i-1]) * 2

        else:
            even_result += int(card_nums[i-1])
    
    result = odd_result + even_result
    result1 = 0

    if result % 10 == 0:
        print('#{} {}'.format(test_case, result1))
    else:
        result1 = 10 - result % 10 
        print('#{} {}'.format(test_case, result1))
