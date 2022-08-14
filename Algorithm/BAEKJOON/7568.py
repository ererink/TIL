# 덩치

# 사람의 수 N 입력
N = int(input())

list_=[]
# 각 사람의 몸무게와 키 입력
for i in range(N):
    weight, height = list(map(int,input().split()))
    # 리스트에 몸무게와 키 저장
    list_.append((weight,height))

for i in list_:
    rank = 1
    for j in list_:
        if i[0] < j[0] and i[1] < j[1]:
                rank += 1
    print(rank, end = " ")
