# 모음의 개수 찾기 

# 오류 코드
word = "HappyHacking"

count = 0

for char in word:
    if char == "a" or "e" or "i" or "o" or "u":
        count += 1

print(count)

# 해결 코드
word = "HappyHacking"

count = 0

for char in word:
    if char in ["a", "e", "i", "o", "u"]: # 대괄호로 리스트를 만들어 준다. 
                                          # =이 아닌 in으로 바꿔준다. 
                                          # 리스트 상태에서 =로 한다면 모음 모두가 해당되기 때문에 0이 출력된다. 
        count += 1

print(count)