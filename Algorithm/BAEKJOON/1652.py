# 누울 자리를 찾아라

n = int(input())                    
metrix = []                         # 행렬 저장
row_cnt = 0                         # 가로 누울 자리 횟수 저장
col_cnt = 0                         # 세로 누울 자리 횟수 저장
check1 = []                         # 가로 입력값 검열 리스트 ('.' or 'X')
check2 = []                         # 세로 입력값 검열 리스트 ('.' or 'X')

for _ in range(n):                  # 행렬 입력
    line = list(input())
    metrix.append(line)
    
for i in range(n):     
    check1.clear()                  # (가로눕기)행 바꿀 시 검열 리스트를 초기화한다
    check2.clear()                  # (세로눕기)행 바꿀 시 검열 리스트를 초기화한다
    for j in range(n): #col 

        #가로눕기
        check1.append(metrix[i][j]) # 각 행의 값을 cheak1 리스트에 넣어준다
    
        if 'X' in check1:           # 만약 'X'가 나온다면
            check1.clear()          # 검열 리스트를 초기화
            
        elif check1.count('.') == 2: # 검열 리스트에 '.'이 두개라면 
            row_cnt += 1            # (가로) 누울 자리 하나 추가
                                    # 2개 이상이 아닌 ==2로 끝내는 이유는 '.'이 3개 이상이 될 경우 cnt가 계속 늘어나기 때문
        # 세로눕기
        check2.append(metrix[j][i]) # 각 열의 값을 cheak2 리스트에 넣어준다
    
        if 'X' in check2:           # 만약 'X'가 나온다면
            check2.clear()          # 검열 리스트를 초기화
            
        elif check2.count('.') == 2: # 검열 리스트에 '.'이 두개라면 
            col_cnt += 1             # (세로)누울 자리 하나 추가
            
print(row_cnt, col_cnt)             # 최종적으로 누울 자리의 개수 출력

