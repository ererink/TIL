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
import sys
from collections import deque

input = sys.stdin.readline

while True:
