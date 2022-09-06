word = input()
word = word.lower()
max_cnt = 0
check = ''

for j in set(word):
    cnt = 0

    if j in word:
        cnt += word.count(j)

    
        if max_cnt < cnt:
            max_cnt = cnt
            check = ''
            check += j
    
        elif max_cnt == cnt:
            check = ''
            check += '?'

print(check.upper())