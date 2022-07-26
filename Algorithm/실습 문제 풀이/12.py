# 12번 문자열 조작하기
# 주어진 문자열 word가 주어질 때, 
# 해당 단어에서 ‘a’를 모두 제거한 결과를 출력하시오.

# 방법 1
from multiprocessing.pool import ApplyResult


word = input()
result = word[1:5]

print(result)

# 방법 2
word = 'apple'
result = ''

for char in 'apple':       # 반복을 위해 for문을 사용한다. 
    if char != 'a': # 만약 a가 아닐 때
        result += char 
print(result)
