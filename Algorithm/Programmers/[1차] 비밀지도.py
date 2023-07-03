# 정답 코드
def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        # 첫번째 지도 이진법 변환
        code1 = bin(arr1[i])[2:]

        temp = ''
        # 이진법으로 변환한 암호의 길이가 n보다 작을 때
        if len(code1) < n:
            # n보다 작은 만큼 길이를 '0'으로 추가
            for k in range(n - len(code1)):
                temp += '0'

        temp += code1
            
        code2 = bin(arr2[i])[2:]
        temp2 = ''
        # 두번째 지도 이진법 변환
        if len(code2) < n:
            for k in range(n - len(code2)):
                temp2 += '0'

        temp2 += code2
        

        chk = ''
        for j in range(n):
            # 둘 중 하나라도 '1'일 경우
            if temp[j] == '1' or temp2[j] == '1':
                # '#'으로 변환
                chk += '#'
            # 둘 다 '0'일 경우
            if temp[j] == '0' and temp2[j] == '0':
                # 공백으로 변환
                chk += ' '
        
        # 한줄씩 answer 리스트에 할당
        answer.append(chk)
        
    return answer

# 시도1
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


