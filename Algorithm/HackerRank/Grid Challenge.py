def gridChallenge(grid):
    m = len(grid[0])

    for i in range(n):
        grid[i] = sorted(grid[i])
    
    for i in range(m):
        for j in range(n-1):
            if grid[j][i] > grid[j+1][i]:
                return 'NO'
    return 'YES'

n = 8
grid = [
    ['eibjbwsp'],
    ['ptfxehaq'],
    ['jxipvfga'],
    ['rkefiyub'],
    ['kalwfhfj'],
    ['lktajiaq'],
    ['srdgoros'],
    ['nflvjznh']
]
answer = gridChallenge(grid)
print(answer)