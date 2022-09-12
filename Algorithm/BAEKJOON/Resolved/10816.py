'''
input = 
    10                          => 숫자 카드의 개수
    6 3 2 10 10 10 -10 -10 7 3  => 숫자 카드
    8                           => 구할 숫자 개수
    10 9 -5 2 3 4 5 -10         => 구할 숫자 
'''

n = int(input())
cards = input().split()
m = int(input())
finding = input().split()

check = []

for i in range(m):
    if finding[i] in cards:
        check.append(cards.count(finding[i]))
    else:
        check.append(0)

print(*check)
