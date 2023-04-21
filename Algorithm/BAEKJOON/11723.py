import sys

N = int(sys.stdin.readline())
S = set()

for i in range(N):
    check = sys.stdin.readline().strip().split()
    if len(check) == 1:
        if check[0] == 'all':
            S = set(range(1, 21))
        else:
            S = set()
    
    else:
        cmd , num = check[0], check[1]
        num = int(num)

        if cmd == 'add':
            S.add(num)
        
        elif cmd == 'remove':
            S.discard(num)

        elif cmd == 'check':
            if num in S:
                print(1)
            else:
                print(0)

        elif cmd == 'toggle':
            if num in S:
                S.discard(num)
            else:
                S.add(num)
        
        