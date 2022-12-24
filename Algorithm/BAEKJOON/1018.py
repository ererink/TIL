'''
[브루트 포스]
체스판 다시 칠하기
지민이는 8×8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다. 
당연히 8*8 크기는 아무데서나 골라도 된다. 지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.
'''

n, m = map(int, input().split())
matrix = []
result = []

for _ in range(n):
    matrix.append(input())

for i in range(n-7):
    for j in range(m-7):
        index1 = 0
        index2 = 0

        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b) % 2 == 0:
                    if matrix[a][b] != 'W':
                        index1 += 1
                    if matrix[a][b] != 'B':
                        index2 += 1
                else:
                    if matrix[a][b] != 'B':
                        index1 += 1
                    if matrix[a][b] != 'W':
                        index2 += 1
        result.append(min(index1, index2))

print(min(result))