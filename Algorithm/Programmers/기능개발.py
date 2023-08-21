import math
def solution(progresses, speeds):
    answer = []
    deploy = []
    n = len(progresses)
    cnt = 1
    prev = 0
    
    for i in range(n):
        rest = 100 - progresses[i]
        # 배포 가능한 날
        chk = math.ceil(rest / speeds[i])
        # 이전값 할당
        if prev == 0:
            prev = chk
        # 이전값과 비교
        else:
            if prev < chk:
                answer.append(cnt) # 이전 배포 개수 할당
                cnt = 1            # 초기화
                prev = chk
            else:
                cnt += 1
                
    if prev != 0:
        answer.append(cnt)
                    
    return answer