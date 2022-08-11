'''
input = 
    12345123
    17772345
    22233331

output = 
    1
    3
    4
'''
for _ in range(3):                          # 3번의 입력을 받는다.
    nums = input()                          # int가 아닌 str으로 입력값을 받는다.
    cnt = 1                                 # 연속된 숫자가 없으면 1로 출력해야 하므로 기본값을 1로 설정한다. 
    max_cnt = 1

    for i in range(1, len(nums)):           # 범위 설정 시 시작값을 1로 설정한다. 비교 시 이전 숫자와 비교하기 위해서. 
        if nums[i] == nums[i-1]:
            cnt += 1                        # 연속된 같은 숫자라면 cnt에 1을 더해준다. 
        
        else:
            max_cnt = max(cnt, max_cnt)     # 같은 숫자가 아니라면 위 구문의 cnt 값을 max_cnt로 옮겨준다. cnt와 max_cnt 중 비교하여 max_cnt에 큰 값을 넣어준다. 
            cnt = 1                         # 다시 남은 숫자를 비교하기 위해 cnt를 1로 초기화한다. 
    
    max_cnt = max(cnt, max_cnt)             # 반복문이 끝나면 다시 연속된 숫자의 개수 중 큰 수를 max_cnt에 넣어준다. 
    print(max_cnt)                          # 연속된 숫자 중 더 많은 개수를 출력한다. 
        