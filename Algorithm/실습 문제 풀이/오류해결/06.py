# 1부터 N까지의 2의 곱 저장하기 

# 오류 코드
N = 10
answer = ()
for number in range(N + 1):
    answer.append(number * 2)

print(answer)

# 해결 코드
N = 10
answer = [] #소괄호()로 이루어진 튜플은 수정을 할 수 없다. append로 값을 추가하기 위해
            # 대괄호[]로 리스트를 만든다. 
for number in range(N + 1):
    answer.append(number * 2)

print(answer)
