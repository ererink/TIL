# 구현
# 그룹 단어 체커

'''
input = 
        4
        aba
        abab
        abcabc
        a

output = 1
'''

n = int(input())
cnt = n

for _ in range(n):
    word = input()


    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            pass
        elif word[i] in word[i + 1:]: #i + 1부터 문자열의 끝까지 탐색한다. 
            cnt -= 1
            break
print(cnt)

'''
input = 
        4
        aba
        abab
        abcabc
        a

print(word[i + 1:])

output = 
        ba
        bab
        ad
        bcabc
        cabc
        acb
'''