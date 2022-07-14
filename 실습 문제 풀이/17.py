# 17번 소문자-대문자 변환하기
# 소문자로 구성된 문자열 word가 주어질 때, 모두 대문자로 바꾸어 표현하시오.
# .upper(), .swapcase() 사용 금지

data = input()

for i in range(len(data)) :
  if 65 <= ord(data[i]) <= 90 :
    print(chr(ord(data[i]) + 32), end='')

  else :
    print(chr(ord(data[i]) - 32), end='')

# 방법 설명
# 1. 알파벳을 숫자로 바꾸고
# 2. 그 숫자를 -32하고
# 3. 다시 숫자를 알파벳으로 바꾼다. 

word = 'banana'
result = 0

for i in word:
  number = ord(i)
  number = number - 32
  result += chr(number)
print(result)