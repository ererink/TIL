
from lib2to3.pgen2.token import RBRACE
from subprocess import BELOW_NORMAL_PRIORITY_CLASS


K, Q, R, B, N, P = map(int, input().split())

K = 1 - K
Q = 1 - Q
R = 2 - R
B = 2 - B
N = 2 - N
P = 8 - P

print(K, Q, R, B, N, P)