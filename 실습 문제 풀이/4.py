# 4번 곱 구하기
# 1부터 n까지의 곱을 구하여 출력하는 코드를 
# 1) while 문 2) for 문으로 각각 작성하시오.

    # for문
mul = 1

for n in range(1, 6):
    mul *= n
  
print(mul)

    # whle문
n = 1
mul = 1

while n <= 5:
    mul *= n
    n += 1
print(mul)