# 9935
# 문자열 폭발

word = input()
bang = input()

while True:
    if bang in word:
        word = word.replace(bang, '')
    
    if bang not in word:
        break
    

if not word:
        print('FRULA')
else: 
    print(word)
'''
시간 복잡도가 각각 O(N)이었기 때문에 O(N^2)가 되어 시간 초과 발생
'''


import sys
input = sys.stdin.readline

word = input().rstrip()
bang = input().rstrip()
check = []
n = len(bang)

for i in word:
    check.append(i)
    if ''.join(check[-n:]) == bang:         # 리스트에 있는 문자열을 합쳐서(.join) 폭발할 문자열과 비교한다.
        del check[-n:]

if not check:
    print('FRULA')
else:
    print(''.join(check))