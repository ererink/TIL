# 음양 더하기

def solution(absolutes, signs):
    
    answer = 0
    
    for i in range(len(absolutes)) :        # 절대값의 원소 개수로 인덱스 위치를 표현해준다.
        
        if signs[i] == False :              # 순회 시 false가 있다면
            answer += (absolutes[i] * -1)   # 절대값 리스트에서의 해당 인덱스 위치 값에 -1을 곱해준 후 (음수값으로 변환)
                                            # answer에 넣어준다. 
        else:
            answer += absolutes[i]          # false가 없다면(true 라면) answer에 넣어준다. 
        
    return answer