# 슈퍼마리오

# 방법 1
mushrooms =[]                       # 입력값을 저장할 리스트
result = 0                          # 더한 값을 저장할 변수

for i in range(10) :                # 10번의 점수(입력값)을 반복해서 
    mushrooms.append(int(input()))  # 버섯 리스트에 넣어준다
    
for j in range(10) :                # 10개의 버섯을 반복해서 더해주며 result에 값을 넣는다.  
    under_result = result           # result의 값을 under_result에 저장해둔다. (100을 넘어갈 상황에 대비하여 원래 값을 저장한다)
    result += mushrooms[j]          # 버섯의 점수들을 result에 넣는다. (합산 점수)
    
    # 100을 넘을 때 
    if result >= 100 :              # 만약 합산 점수가 100을 넘는다면
        over = result - 100         # 얼마나 넘었는지 계산
        under = 100 - under_result  # 얼마나 안넘었는지 계산
        if over <= under:           # 만약 under 더 크다면 (100을 넘지 않은 합산 점수의 차)
            print(result)           # 100을 넘은 점수를 출력한다. 
            break                   # over와 under의 값이 클수록 100과 멀어지기 때문에 더 작은 것을 택한다.
        else:
            print(under_result)
            break
    
else:                               # 다 더해도 100을 넘지 않으면 그 값을 그냥 출력한다. 
    print(result)


# 방법 2
for i in range(1, 11):
    score = int(input())
    before_result = result

    result += score

    if result >= 100:
        if (result - 100) > (100 - before_result):
            result = before_result
        break

print(result)