'''
input = 
4 4
#..#
..X.
..X.
#XX#

output = 
1
1
2
1
0

# = 빌딩
X = 주차
. = 빈공간 

해빈의 차 = 2행 2열 

출력값 조건
1. '.' 4개 
2. '.' 3개, 'X' 1개
3. '.' 2개, 'X' 2개
4. '.' 1개, 'X' 3개
5. 'X' 4개
'''

n, m = map(int, input().split())

parking_lot = []                                    # 입력값 행렬을 넣어줄 변수 리스트
breaking_car1 = 0                                   # 출력값 조건들에 맞는 변수 생성
breaking_car2 = 0
breaking_car3 = 0
breaking_car4 = 0
breaking_car5 = 0
check = []                                          # 탐색 시 값들을 담아서 확인해줄 리스트 생성

for _ in range(n):                                  # 입력값 받기
    parking_lot.append(list(input()))               # 입력값을 parking_lot 리스트에 넣어준다. 

for i in range(n-1):                                # 전체 행렬, 탐색 시 범위를 벗어나지 않도록 (n-1)로 범위 설정
    for j in range(m-1):                            # i, j = 기준 행/열
        check.clear()                               # 하나의 행/열이 끝날 시 확인하는 리스트를 비워준다. 

        for a in range(i, i + 2):                   # 해빈의 차(2행 2열) 만큼 탐색한다.
            for b in range(j, j + 2):               # a, b = 탐색 행/열
            
                check.append(parking_lot[a][b])
                
                if check.count('.') == 4:
                    breaking_car1 += 1              # 조건 1
    
                elif check.count('.') == 3 and check.count('X') == 1:
                    breaking_car2 += 1              # 조건 2
                    
                elif check.count('.') == 2 and check.count('X') == 2:
                    breaking_car3 += 1              # 조건 3
                    
                elif check.count('.') == 1 and check.count('X') == 3:
                    breaking_car4 += 1              # 조건 4
                    
                elif check.count('X') == 4:
                    breaking_car5 += 1              # 조건 5

print(breaking_car1)
print(breaking_car2)
print(breaking_car3)
print(breaking_car4)
print(breaking_car5)