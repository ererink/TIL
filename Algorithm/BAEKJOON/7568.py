# 덩치

# 사람의 수 N 입력
N = int(input())

list_=[]
# 각 사람의 몸무게와 키 입력
for i in range(N):
    weight, height = list(map(int,input().split()))
    # 리스트에 몸무게와 키 저장
    list_.append((weight,height))

ranks = [0] * N
# 모든 사람을 비교하기 위한 이중반복문
for a in range(N):
    A = list_[a]
    for b in range(N):
        B = list_[b]

        # 덩치가 큰지 확인
        if A[0] > B[0] and A[1] > B[1]:
            ranks[b] += 1

for rank in ranks:
    print(rank+1, end=' ')
