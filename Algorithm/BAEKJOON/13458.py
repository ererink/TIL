'''
input = 
    1       => 시험장 개수
    1       => 응시자 수 
    1 1     => 총감독관/부감독관이 감시할 수 있는 응시자 수

필요한 감독관의 최소 수
'''

n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())
num = 0

for i in a:
    i = i - b
    num += 1
    if i > 0:
        num += abs(i // c)

        if abs(i % c) >= 1:
            num += 1

print(num)