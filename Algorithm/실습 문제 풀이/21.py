# 주어진 숫자를 뒤집은 결과를 출력하시오. 
# * 문자열이 아닌 숫자로 활용. str() 사용 금지

#str() 사용
number = 1234

print(int(str(number)[::-1]))

# 내 답안
def f(n):
    if n <= 0: return
    print(n % 10, end='')
    f(n//10)

f(1234) 
# 출력 4321

# 모범 답안 
result = 0

while number:
   result *= 10 # 이전 결과에 10을 곱하고
   result += number % 10 # 나머지를 더해주고
   number //= 10 # number를 깎는다. 