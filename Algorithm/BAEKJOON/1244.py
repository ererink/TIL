'''
1 == 남학생: 배수의 스위치를 바꾼다.
2 == 여학생: 좌우 대칭되는 스위치를 바꾼다.

input = 
    8                   => 스위치 개수
    0 1 0 1 0 0 0 1     => 스위치 상태
    2                   => 학생 수
    1 3                 => 학생의 성별, 받은 수
    2 3                 => 학생의 성별, 받은 수

'''

s = int(input())
switch_state = input()
n = int(input())

for _ in range(n):
    g, o = map(int, input().split())                         # o - 1 = index

    for i in range(s):
        print(type(i))
        # 남학생
        if g == 1:
            if i % o == 0:                      # 배수일 때
                # 스위치 on일 때
                if switch_state[i - 1] == 1:
                    switch_state[i - 1] = 2  

                # 스위치 off일 때 
                else:
                    switch_state[i - 1] = 1

        # 여학생
        if g == 2:
            # i - 1이 기본
            if switch_state[i - 2] == switch_state[i]:      # i 좌우 값이 대칭될 때(일치)
                # 스위치 on일 때
                if switch_state[i - 2] == 1:                            
                    switch_state[i - 2] = 2                 # 대칭되므로 같이 바꿔준다. 
                    switch_state[i] = 2
                
                # 스위치 off일 때
                else:
                    switch_state[i - 2] = 1
                    switch_state[i] = 1

print(switch_state)