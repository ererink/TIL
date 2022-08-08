# 일곱 난쟁이

dwarfs = []                                             # 난쟁이의 키를 저장할 리스트 변수
for x in range(9):                                      # 9번의 난쟁이 키 값을 받는다.
    input_ = int(input())
    dwarfs.append(input_)                               # 난쟁이의 키 값을 리스트에 하나씩 넣어준다. 


sum_ = sum(dwarfs)                                      # 리스트에 저장된 9명의 난쟁이 키를 모두 합산한다. 

for i in range(9):                                      # 전체 9명의 난쟁이를 순회한다. 
    for j in range(i + 1, 9):                           # 2명의 난쟁이를 빼주기 위한 탐색
        if sum_ - (dwarfs[i] + dwarfs[j]) == 100:       # 만약 9난쟁이를 모두 더한 값에 2명의 난쟁이 키 값을 뺀 값이 100이라면
            not_d1 = dwarfs[i]                          # 7 난쟁이에서 제외된 2명의 난쟁이 변수에 저장한다.
            not_d2 = dwarfs[j]

dwarfs.remove(not_d1)                                   # 제외할 2명의 난쟁이 키 값을 리스트에서 제거한다.
dwarfs.remove(not_d2)
dwarfs = sorted(dwarfs)                                 # 오름차순으로 정리한다. 

for k in dwarfs:                                        # 리스트에 있는 7난쟁이의 키 값을 하나씩 출력한다. 
    print(int(k))