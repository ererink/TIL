import sys

t = int(input())
for test_case in range(1, t + 1):
    n = int(input())
    cards = list(input().split())
    shuffle1 = []
    shuffle2 = []

    if len(cards) % 2 == 0:                         # 카드의 수가 짝수일 경우 정확히 반을 나누어서 각 리스트에 저장한다. 
        for i in range(len(cards) // 2):
            i = 0
            shuffle1.append(cards[i])
            cards.remove(cards[i])
    else:
        for i in range((len(cards) // 2) + 1):      # 카드의 수가 홀수일 경우 shuffle1에 카드 한 장이 더 들어간다. 
            i = 0
            shuffle1.append(cards[i])
            cards.remove(cards[i])

    
        

    for j in range(len(cards)):
        shuffle2.append(cards[j])
    
    perfect_shuffle = []
    while len(shuffle1) != 0 or len(shuffle2) != 0:
        if len(shuffle1) > 0:
            perfect_shuffle.append(shuffle1.pop(0))
        if len(shuffle2) > 0 :
            perfect_shuffle.append(shuffle2.pop(0))

    print(f'#{test_case}', *perfect_shuffle)

sys.stdin = open("_퍼펙트셔플.txt")
