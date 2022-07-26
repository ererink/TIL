# 10번 5의 개수 구하기
# 주어진 리스트의 요소 중에서 5의 개수를 출력하시오.

# count() 활용
numbers = [7, 17, 10, 5, 4, 3, 17, 5, 2, 5]

print(numbers.count(5))

# if문 활용
numbers = [7, 17, 10, 5, 4, 3, 17, 5, 2, 5]
cnt = 0

for i in numbers:
    if i == 5:
        cnt += 1

print(cnt)