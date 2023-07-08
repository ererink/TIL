def solution(name, yearning, photo):
    answer = []
    yearning_dict = {}
    n = len(name)
    
    for i in range(n):
        yearning_dict[name[i]] = yearning[i]
    
    m = len(photo)
    for i in range(m):
        temp = 0
        for j in range(len(photo[i])):
            if photo[i][j] in yearning_dict:
                temp += yearning_dict.get(photo[i][j])
                
        answer.append(temp)
    return answer