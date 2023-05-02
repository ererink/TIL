def solution(n, arr1, arr2):
    answer = [list() for _ in range(n)]
    chk = ''
    chk1 = [list() for _ in range(n)]
    chk2 = [list() for _ in range(n)]

    # 첫 번째 지도
    for i in arr1:
        line = bin(i)
        # 2진수 n자리 만들기
        if len(line) > n + 1:
            # 뒤부터 n자리 슬라이싱
            line = line[-n:]
        for j in line:
            if j != 'b':
                if j == '0':
                    chk += ' '
                elif j == '1':
                    chk += '#'
                    
        chk1.append(chk)
        chk=''
    
    # 두 번째 지도
    for i in arr2:
        line = bin(i)
        if len(line) > n + 1:
            temp = line[-n:]
            
        for j in line:
            if j != 'b':
                if j == '0':
                    chk += ' '
                elif j == '1':
                    chk += '#'
        chk2.append(chk)
        chk=''
    
    # 지도 합치기
    for i in range(n):
        line = ''
        for j in range(n):
            if chk1[i][j] == '#' or chk2[i][j] == '#':
                line += '#'
            else:
                line += ' '
        answer[i].append(line)
        
    return answer