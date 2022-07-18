# 평균 구하기

# 오류 코드
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
count = 0

for number in number_list:
    total += number
count += 1

print(total // count)

# 해결 코드
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
count = 0

for number in number_list:
    total += number
    count += 1 # for문에 속하여 실행하여야 하기 때문에 들여쓴다. 

print(total / count) # //는 몫만 나오기 때문에 /(나누기)로 실행하여 소수점까지 출력한다. 