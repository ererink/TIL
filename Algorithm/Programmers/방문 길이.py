def solution(dirs):
    answer = 0
    nx = 0; ny = 0
    visited = []
    visited.append((0, 0))

    for i in dirs:
        x, y = nx, ny
        
        if i == 'U':
            nx += 1
        elif i == 'D':
            nx -= 1
        elif i == 'R':
            ny += 1
        else:
            ny -= 1

        if -5 <= nx <= 5 and -5 <= ny <= 5:
            if (x, y, nx, ny) not in visited and (nx, ny, x, y) not in visited:
                visited.append((x, y, nx, ny))
                answer += 1
        else:
            # 원상복귀
            nx, ny = x, y  

            
    return answer