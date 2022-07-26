# 15번 문자의 위치 구하기 
# 문자열 word가 주어질 때, 해당 문자열에서 
# a 가 처음으로 등장하는 위치(index)를 출력해주세요.
# a 가 없는 경우에는 -1을 출력해주세요.
# find() index() 메서드 사용 금지

word = input()
result = 0

for i in word:
    if i == 'a':
        break
    result += 1
  
else:
  result == len(word)
  result = -1
      
print(result)

# 방법 2
word = input()

for i in range(len(word)): # 인덱스로 접근해야 한다. 그래서 range(len())를 사용해야 한다.\
  if word[i] == 'a':
    print(i) # i == index
    break

  else:
    print(-1)



# 추가 문제 
# 문자열 word가 주어질 때, 해당 문자열에서 a 의 모든 위치(index)를 출력해주세요.
# find() index() 메서드 사용 금지

word = input()

for i in range(len(word)):
  if word[i] == 'a':
    print(i, end = " ")

# 방법 2. 리스트를 담는 방법
word = input()
result = []
for i in range(len(word)):
  if word[i] == 'a':
    result.append(i)
    
print(result)