# 7번 최솟값 구하기
# 주어진 리스트 numbers에서 최솟값을 구하여 출력하시오.
# min() 함수 사용 금지

numbers = [0, 20, 100]
minimum = numbers[0]

for i in numbers:
  if i < minimum:
    minimum = i

print(minimum)