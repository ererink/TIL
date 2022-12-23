# 단어 정렬
'''
알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

길이가 짧은 것부터
길이가 같으면 사전 순으로

input = 13
        but
        i
        wont
        hesitate
        no
        more
        no
        more
        it
        cannot
        wait
        im
        yours

output = i
        im
        it
        no
        but
        more
        wait
        wont
        yours
        cannot
        hesitate
'''

n = int(input())

words = []
for _ in range(n):
    words.append(input())
words = list(set(words))      # 중복제거, set()을 사용하면 리스트가 없어지므로 다시 리스트를 씌워서 sort() 사용

words.sort()            # 알파벳순 정렬
words.sort(key=len)     # 길이순 정렬

for i in words:
        print(i)