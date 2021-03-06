# 영문 소문자(a ~ z) 1개가 입력되었을 때,
# a부터 그 문자까지의 알파벳을 순서대로 출력한다.

a = ord(input())
s = ord('a')

while a >= s:
  print(chr(s), end = ' ')
  s += 1

# ord()는 해당 문자에 해당하는 유니코드의 정수로 반환한다. (문자 -> 정수)
# chr()는 해당 정수에 해당하는 유니코드의 문자로 반환한다. (정수 -> 문자)

# a는 입력값을 정수로 바꾼다.
# s는 'a'값을 정수로 바꾼다. 

# 입력값(a)가 s인 'a'보다 크지만 같을 때 멈추게된다. 
# 입력값이 f라면 f가 될 때 까지 s에 1을 더해준다. 