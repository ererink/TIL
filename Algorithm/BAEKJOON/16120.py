# PPAP

word = input()
stack = []
ppap = ['P', 'P', 'A', 'P']
for i in word:
    stack.append(i)
    
    # stack에 할당된 값이 PPAP일 때 맨 앞의 P를 남겨두고 나머지 3개의 문자를 빼준다.
    # 일치한다면 PPAP를 P로 변환하는 작업
    if stack[-4:] == ppap:
        stack.pop()
        stack.pop()
        stack.pop()
        
# 하나의 P만 stack에 남아도 해당 문자가 PPAP 변환이 가능하기 때문에 PPAP를 출력한다.
if stack == ppap or stack == ['P']:
    print('PPAP')
else:
    print('NP')