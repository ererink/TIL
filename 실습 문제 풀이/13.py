# 13번 문자열 조작하기
# 주어진 문자열 word가 주어질 때, 
# 해당 단어를 역순으로 뒤집은 결과를 출력하시오.

# 방법 1
word = 'apple'
result = word[::-1]

print(result)

# 방법 2
word = 'apple'
result = '' # 비어있는 문자열을 만든다.
for char in word:
    result = char + result # 거꾸로 더한다.

print(result)

# 방법 3
print(''.join(reversed(word)))

# 방법 4 (index) -> 익숙해지면 나중에 알고리즘 코드 풀기 좋다. 
word = 'apple'

for i in range(len(word)):
    print(word[len(word)-i])