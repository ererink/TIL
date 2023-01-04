'''
그리디

신입 사원
'''
import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    applicant = [list(map(int, input().split())) for _ in range(n)]
    rank = sorted(applicant)    # 서류점수 기준으로 정렬
    top = 0
    admit = 1   # 이미 첫번째 지원자는 합격
    
    for i in range(1, len(rank)):       # +1 순서 지원자와 그 앞 순서 지원자 면접 접수 비교
        if rank[i][1] < rank[top][1]:   # 앞순서 지원자의 면접점수가 더 크면 합격자 수 +1
            top = i                     # 다음 지원자와 비교하기 위해 (이동)
            admit += 1
            
    print(admit)