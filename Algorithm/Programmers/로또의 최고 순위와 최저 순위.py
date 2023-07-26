def solution(lottos, win_nums):
    answer = []
    win_cnt = 0
    
    for i in range(6):
        # 이미 맞은 로또 번호 카운트
        if lottos[i] in win_nums:
            win_cnt += 1
            
    lose = win_cnt
    win_cnt += lottos.count(0)
    
    if win_cnt == 6:
        answer.append(1)
    elif win_cnt == 5:
        answer.append(2)
    elif win_cnt == 4:
        answer.append(3)
    elif win_cnt == 3:
        answer.append(4)
    elif win_cnt == 2:
        answer.append(5)
    else:
        answer.append(6)
        
    if lose == 6:
        answer.append(1)
    elif lose == 5:
        answer.append(2)
    elif lose == 4:
        answer.append(3)
    elif lose == 3:
        answer.append(4)
    elif lose == 2:
        answer.append(5)
    else:
        answer.append(6)
        
    
    return answer