# 1264 모음의 개수

vowels = 'aeiouAEIOU'

for _ in range(99999):          # 입력값 받기 
    sentence = input()          

    if sentence == '#':         # 입력값에 '#'이 나오면 입력 받기 중단
        break

    vowels_cnt = 0              # 모음의 개수를 세는 변수
    for i in sentence:          # 입력값은 i에 넘겨주고,
        if i in vowels:         # i가 모음 목록에 포함된다면
            vowels_cnt += 1     # 모음 개수가 1개 늘어난다.
    print(vowels_cnt)
    

