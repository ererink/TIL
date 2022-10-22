def solution(babbling):
    answer = 0
    word = ['aya', 'ye', 'woo', 'ma']
    
    for i in babbling:
        for j in word:

            if j * 2 not in i: 
                i = i.replace(j, '')
        if len(i) == 0:
            answer += 1
                            
                
    return answer