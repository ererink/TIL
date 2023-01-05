# 폴리오미노

# 방법 1
board = input().split('.')                      # .을 기준으로 나눠 받는다
answer = ''                                     # 폴리오미노로 바꿔준 후 넣어주는 변수

for i in board:                                 # . 기준으로 나눠 받은 입력값을 i에 하나씩 던져줌 (X 묶음으로)
    if len(i) % 2 > 0:                          #  짝수가 아니면 -1 출력
        print(-1)
        break
                                                # 위 반복문으로 X의 개수가 짝수인 묶음만 확인하게 됨
    if len(i) >= 4:                             # X가 4개 이상이므로 폴리오미노 확인
        if len(i) % 4 != 0:                     # 4개로 나눠 떨어지지 않을 때
            answer += 'AAAA' * (len(i) // 4)    # 4의 배수인 X 묶음을 일단 AAAA로 바꿔줌
            answer += 'BB'                      # 나머지를 BB로 바꿔줌 (어차피 짝수이므로 나머지를 무조건 BB로 넣어줄 수 있음)
        else:                                   # 4개로 나눠 떨어질 때
            answer += 'AAAA' * (len(i) // 4)    # 4개로 나눠떨어지는 몫만큼 AAAA로 바꿔주기
            
    elif len(i):                                # X가 4개 이상이 아닐 때        
        answer += 'BB'                          # BB로 바꿔주기
    answer += '.'                               # answer에 넣어줄 때 마다 폴리오미노 끝에 .이 붙게 된다. 이는 .으로 받은 입력값을 그대로 출력해야하므로 필요
                                                # 입력값이 '.'일때는 "" 빈칸으로 받게 되는데 이때 이 연산으로 인해 .이 answer에 들어가게 됨

else:
    print(answer[:-1])                          # answer에 할당될 때 폴리오미노 끝에 .이 붙기 때문에 마지막 문자열은 빼고 출력
    

# 방법 2 (replace)
board = input()

board = board.replace("XXXX", "AAAA")           # X가 4개 연속으로 있는 문자열을 AAAA로 바꿔주기
board = board.replace("XX", "BB")               # X가 2개 연속으로 있는 문자열을 BB로 바꿔주기

if 'X' in board:                                # X가 남아있는 경우는 홀수일 때 이므로 -1을 출력
    print(-1)
    
else:
    print(board)