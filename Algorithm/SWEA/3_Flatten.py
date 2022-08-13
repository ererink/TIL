import sys

for test_case in range(1, 11):

    t = int(input())

    boxes = list(map(int, input().split()))

    while t != 0:
        boxes = sorted(boxes)
        boxes[-1] -= 1
        boxes[0] += 1
        t -= 1

    boxes = sorted(boxes)
    
    print(f'#{test_case}', max(boxes) - min(boxes))


sys.stdin = open("_Flatten.txt")
