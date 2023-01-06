def solution(id_pw, db):
    answer = ''
    
    for i in range(len(db)):
        if db[i][0] == id_pw[0]:
            if db[i][1] == id_pw[1]:
                answer += 'login'
                break
            else:
                answer += 'wrong pw'
                break
    
    if len(answer) == 0:
        answer += 'fail'
    return answer