# 유니크 

# try1
n = int(input())
matrix = []
score = 0

for _ in range(n):          # 열 이동
    line = list(map(int, input().split()))
    matrix.append(line)

for i in range(n):          # 행 이동
    for j in range(3):
        print(matrix[i])

        if matrix[i][j] not in matrix[i]:
            score += int(matrix[i][j])
        else: 
            continue
print(score)

# answer
n = int(input())
score = [[], [], []]
sum = []                                    # 각 최종 점수 저장소
 
for i in range(n):
    a, b, c = map(int, input().split())
    score[0].append(a)                      # 첫 번째 점수 저장소
    score[1].append(b)                      # 두 번째 점수 저장소
    score[2].append(c)                      # 세 번째 점수 저장소 
    
for i in range(n):
    get = 0                                 # 임시적으로 합계점수를 넣을 저장소 
    for j in range(3):
        if score[j].count(score[j][i]) == 1: # 각자 적은 점수가 유일하다면 
            get += score[j][i]              # 해당 점수를 get에 저장
    sum.append(get)                         # 최종 점수를 sum 리스트에 저장

for i in sum:                               # 각 최종 점수를 순차적으로 출력 
    print(i)

