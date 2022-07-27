# 대각선 출력하기
# 주어진 텍스트를 그대로 출력하세요.

# 출력
# #++++
# +#+++
# ++#++
# +++#+
# ++++#

for i in range(5):
    for j in range(5):
        if i == j:
            print('#', end='')
        else:
            print('+', end='')
    print()