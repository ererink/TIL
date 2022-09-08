remove_ = 'CAMBRIDGE'

word = input()
answer = ''
for i in word:
    if i in remove_:
        continue
    else:
        answer += i 

print(answer)