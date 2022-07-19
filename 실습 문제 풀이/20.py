# 정수 number가 주어질 때, 각 자릿수의 합을 구해서 출력하세요. 

n = str(input()) #입력 123
add = 0

for i in range(len(n)):
    add += int(n[i])

print(add)

# 출력 6

# n을 문자열로 바꿔서 n에 저장.
# n의 길이 만큼 반복하는 i, 
# 그동안 n의 i 인덱스 값을 add에 계속 더해준다. 
# (더할 때는 int로 바꿔줘야 연산가능)

# 모범 답안 (나머지 더하기) (10으로 나눌 때 3, 2, 1이 남기 때문에)

number = 123
result = 0

while number: #number가 0일 때 멈춘다. 
              #int는 0일 때 false이기 때문이다.
    result += number % 10 # 몫은 다음 number가 되고, 나머지는 더해나간다. 
                          # 나머지를 먼저 기록해야한다. 
    number //= 10 

print(result)

# divmod
result, remainder = divmod(number, 10) #divmod(x,y)는 x를 y로 나누고 결과를 튜플로 반환한다. (몫, 나머지)
result += remainder

print(result)