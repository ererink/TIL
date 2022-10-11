'''
input = 
    A1 A2 5 => 킹 위치, 돌 위치, 움직이는 횟수
    B
    L
    LB
    RB
    LT

output = 
    A1
    A2

R : 한 칸 오른쪽으로         (0, 1)
L : 한 칸 왼쪽으로          (0, -1)
B : 한 칸 아래로            (1, 0)
T : 한 칸 위로             (-1, 0)
RT : 오른쪽 위 대각선으로     (-1, 1)    
LT : 왼쪽 위 대각선으로       (1, -1)
RB : 오른쪽 아래 대각선으로    (1, 1)
LB : 왼쪽 아래 대각선으로      (-1, -1)
'''
king, stone, n = input().split()
k = list(map(int, [ord(king[0]) - 64, king[1]]))
s = list(map(int, [ord(stone[0]) - 64, stone[1]]))
move = {
    'R': [1, 0], 
    'L': [-1, 0],
    'B': [0. -1],
    'T': [0, 1],
    'RT': [1, 1],
    'LT': [-1, 1],
    'RB': [1, -1], 
    'LB': [-1, -1]
}

for i in range(int(n)):
    m = input()
    nx = k[0] + move[m][0]
    ny = k[1] + move[m][1]
    if 0 < nx <= 8 and 0 < ny <= 8:
        if nx ==  s[0] and ny == s[1]:
            sx = s[0] + move[m][0]
            sy = s[1] + move[m][1]
            if 0 < sx <= 8 and 0 < sy <= 8:
                k = [nx. ny]
                s = [sx, sy]
            
            else:
                k = [nx, ny]
                
print(f'{chr(k[0] + 64)}{k[1]}')
print(f'{chr(s[0] + 64)}{s[1]}')