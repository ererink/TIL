# 1차 시도
def solution(n, left, right):
    new_arr = []
    idx = 0
    for i in range(n):
        for j in range(n):
            if idx >= left and idx <= right:
                if i + 1 > j + 1:
                    new_arr.append(i + 1)
                else:
                    new_arr.append(j + 1)
            idx += 1

    return new_arr