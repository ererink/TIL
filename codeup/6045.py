# 정수 3개를 입력받아 합과 평균을 출력해보자.

# 잘못된 답
a, b, c = map(int, input().split())

print((a + b + c), (a + b + c) / 3)
    # 정답이 아닌 이유는 소수점 두자리까지 출력되도록 하지 않아서.
    
# 정답
a, b, c = map(int, input().split())
avg = (a+b+c)/3

print(a+b+c)
print("%0.2f" % avg)
