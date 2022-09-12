board = [[0] * 15 for _ in range(5)]

for i in range(5):
    word = list(input())
    for j in range(len(word)):
        board[i][j] = word[j]

for i in range(15):
    for j in range(5):
        if board[j][i] == 0:
            continue
        
        else:
            print(board[j][i], end='')