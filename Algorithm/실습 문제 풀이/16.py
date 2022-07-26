# 16번 모음 등장 여부 확인하기
# 문자열 word가 주어질 때, 해당 문자열에서 모음의 갯수를 출력하시오.
# 모음 : a, e, i, o, u 
# count() 사용 금지

# 방법 1
word = input()
result = 0

for i in word:
    if i in ['a', 'e', 'i', 'o', 'u']: # 리스트로 만들어준다.
      result += 1
      
print(result)

# 방법 2
word = input()
result = 0

for i in word:
    if i in 'aeiou':
      result += 1
      
print(result)

# 잘못된 방법
   # if i == 'a' or 'e' or 'i' or 'o' or 'u': 
      # a만 계속 보게된다
  # 이것을 고쳐보면
  # if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u': 
