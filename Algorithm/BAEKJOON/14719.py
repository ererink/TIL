# 빗물

h, w = map(int, input().split())
blocks = list(map(int, input().split()))

water = 0
# 고여있는 빗물 구하기
for i in range(1, w - 1):
    left = max(blocks[:i])      # 왼쪽에서 제일 큰 수
    right = max(blocks[i + 1:]) # 오른쪽에서 제일 큰 수

    s = min(left, right)    # 두번째로 큰 수 (빗물이 고이는 최대 범위)

    if blocks[i] < s:       # 두번째로 큰 수보다 작을 때 빗물이 고이는 양
        water += (s - blocks[i])

print(water)