# 3번 합 구하기
# 1부터 n까지의 합을 구하여 출력하는 코드를 1) while 문 2) for 문으로 각각 작성하시오.
# sum() 함수 사용 금지

    # for문
sum = 0

for n in range(1, 11):
    sum += n
print(sum)

    # While문
n = 1
sum = 0

while n <= 10:
    sum += n
    n += 1
print(sum)