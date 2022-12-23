'''
나이순 정렬

회원들을 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬

3
21 Junkyu
21 Dohyun
20 Sunyoung

20 Sunyoung
21 Junkyu
21 Dohyun
'''

n = int(input())

accounts = []
for _ in range(n):
    age, name = map(str, input().split())
    age = int(age)
    accounts.append((age, name))

accounts.sort(key=lambda x : x[0]) # age만 비교하기 위해

for i in accounts:
    print(i[0], i[1])               # age, name 따로 출력
