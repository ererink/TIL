T = int(input())
for test_case in range(1, T + 1):
    card_nums = input().split()
    result=[]
    for i in card_nums:
        result += i
    
        if result[0] == '3' or '4' or '5' or '6' or '9': 
            if len(result) == 16:
                print('#{} {}'.format(test_case, '1'))
            elif '-' in result:
                for _ in result:
                    result.remove('-')
                    
                    if len(result) == 16:
                        break
                    
                print('#{} {}'.format(test_case, '1'))
            
            else:
                print('#{} {}'.format(test_case, '0'))
        else:
            print('#{} {}'.format(test_case, '0'))
