# 자릿수 더하기 

n = input() # str으로 받기 
result = 0

for i in n:
    result += int(i) # int로 변환하며 더해주기
print(result)