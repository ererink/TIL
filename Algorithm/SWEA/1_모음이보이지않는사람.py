import sys

vowel = ['a', 'e', 'i', 'o', 'u']
t = int(input())
for test_case in range(1, t + 1):
    s = list(input())
    without_vowel = ''

    for i in range(len(s)):
        if s[i] in vowel:
            continue
        without_vowel += s[i]
    
    print('#{} {}'.format(test_case, without_vowel))

sys.stdin = open("_모음이보이지않는사람.txt")
