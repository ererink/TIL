# 다이얼

# 1 - 2초, 2 - 3초

alpa_list = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
word = input()
time = 0

for i in word:
    for j in alpa_list:
        if i in j :
            time += alpa_list.index(j) + 3   # alpa_list에서의 0의 기본 시간값은 3이다. 

print(time)