# 14번 
# 문자열 word가 주어질 때, 해당 문자열에서 a 개수를 구하세요.
# count() 메서드 사용 금지

word = input()
result = 0

for i in word: # i는 이름을 붙여주는 것이다. 
               # word의 요소를 하나씩 던져주는 것이다. 
    if i == 'a':
      result += 1
      
print(result)
