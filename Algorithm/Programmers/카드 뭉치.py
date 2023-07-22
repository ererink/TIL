# 1차
def solution(cards1, cards2, goal):
    answer = ''
    n = len(goal)
    success = []

    for i in range(n):
        # 탐색 및 확인하려는 문자
        check = goal[i]
        # cards1과 cards2를 하나씩 꺼내 맞는 문자가 있는지 확인
        flag = 0
        for j in cards1:
            # 이미 success에 할당한 경우 for문 탈출
            if flag == 1:
                break
                
            if j == check:
                success.append(j)
                cards1.remove(j)
                flag = 1
                break

            # cards1에 일치하는 단어가 없을 경우 cards2 탐색 실행
            else:
                for k in cards2:
                    if k == check:
                        success.append(k)
                        cards2.remove(k)
                        flag = 1
                        break
                        
                    else:
                        answer = 'No'
                        return answer
                    
            # success에 아무것도 할당되지 않은 경우 함수 종료             
            if flag == 0:
                answer = 'No'
                return answer
            
    # 한번 더 확인
    if goal == success:
        answer = 'Yes'
    else:
        answer = 'No'
    
    return answer