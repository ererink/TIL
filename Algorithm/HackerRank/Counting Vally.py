def countingValleys(steps, path):
    answer = 0
    level = 0 

    for i in range(steps):
        if path[i] == 'D':
            level -= 1
        else:
            level += 1

        if level == 0 and path[i] == 'U':
            answer += 1
            
    return answer
