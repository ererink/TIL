import sys

'''
총점 = 중간(35%) + 기말(45%) + 과제(20%)
'''
# 입력
t = int(input())
for test_case in range(1, t+1):
    n, k = map(int, input().split())
    score = []
    rank = []
    grade = ['A+', 'A0', 'A-','B+', 'B0', 'B-','C+', 'C0', 'C-', 'D0']
    
    for i in range(n):
        a, b, c = map(int, input().split())
        # 점수 계산
        result = (round((a * (35/100)) + (b * (45/100)) + (c * (20/100))))
        score.append(result)
        
    k_score = score[k-1]

    rank = sorted(score, reverse=True)

    print('#{} {}'.format(test_case, grade[rank.index(k_score) // (n//10)]))

sys.stdin = open("_조교의성적매기기.txt")
