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
# 0과 1을 바꾸는 함수 만들기 
def change(o):
    if switch_state[o] == 0:
        switch_state[o] = 1
    else:
        switch_state[o] = 0
    return

s = int(input())
switch_state = [-1] + list(map(int, input().split()))
n = int(input())    # 학생 수

for _ in range(n):
    g, o = map(int, input().split())                         # o - 1 = index

    # 남학생
    if g == 1:
        for i in range(o, s + 1, o):        # range(start, stop, step)
            change(i)

    # 여학생
    else:
        change(o)                               # 해당 인덱스 자리의 스위치 상태를 일단 바꾸기
        for j in range(s // 2):
            if o + j > s or o - j < 1:
                break

            if switch_state[o + j] == switch_state[o - j]:
                switch_state[o + j] = 1 - switch_state[o + j]
                switch_state[o - j] = 1 - switch_state[o - j]
            
            else:
                break

for k in range(1, s + 1):
    print(switch_state[k], end = ' ')
    if k % 20 == 0:
        print()
