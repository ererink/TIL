'''
[2차원 배열]

행렬 덧셈
N*M크기의 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 프로그램을 작성하시오.


input = 3 3     => N, M
        1 1 1   
        2 2 2
        0 1 0   => 첫번째 행렬
        3 3 3
        4 4 4
        5 5 100 => 두번째 행렬

output = 4 4 4
        6 6 6
        5 6 100
'''

N, M = map(int, input().split())

matrix1 = [[input().split()] * M for _ in range(N)]
matrix2 = [[input().split()] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        print(int(matrix1[i][j][j]) + int(matrix2[i][j][j]), end=" ")
    print()