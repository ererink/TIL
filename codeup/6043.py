# 실수 2개(f1, f2)를 입력받아
# f1 을 f2 로 나눈 값을 출력해보자. 
# 이 때 소숫점 넷째자리에서 반올림하여 무조건 소숫점 셋째 자리까지 출력한다.

a, b = map(float, input().split())
result = a / b

print(format(result,".3f")) 

# ".3f" or '%.3f'는 실수를 소숫점 3자리까지 표현한다.