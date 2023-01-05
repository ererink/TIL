def solution(array, commands):
    answer = []
    check = []
    
    for i in range(len(commands)):
        check.append(array[int(commands[i][0]) - 1:int(commands[i][1])])
        check[i] = sorted(check[i])
        answer.append(check[i][int(commands[i][2]) - 1])
        
    return answer