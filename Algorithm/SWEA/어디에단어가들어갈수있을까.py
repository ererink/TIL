import sys

t = int(input())
for test_case in range(1, t + 1):
    n, k = map(int, input().split())
    
    metrix = []
    for _ in range(n):                      # 배열 만들기
        metrix.append(list(input().split()))
    
    word = 0
    check1 = []
    check2 = []
    for i in range(n):
        check1.clear()
        check2.clear()
        
        for j in range(n):
            # 가로
            check1.append(metrix[i][j])

            if check1.count('1') > k:
                check1.clear()
                word -= 1
                
            elif '0' in check1:
                check1.clear()
            
            elif check1.count('1') == k:
                word += 1
                
            # 세로
            check2.append(metrix[j][i])

            if check2.count('1') > k:
                check2.clear()
                word -= 1
                
            elif '0' in check2:
                check2.clear()
            
            elif check2.count('1') == k:
                word += 1

    print('#{} {}'.format(test_case, word))

sys.stdin = open("_어디에단어가들어갈수있을까.txt")
