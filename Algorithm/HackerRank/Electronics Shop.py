def getMoneySpent(keyboards, drives, b):
    max_amount = 0
    for i in range(n):
        cnt = keyboards[i]
        for j in range(m):
            cnt += drives[j]
            if max_amount < cnt and cnt <= b:
                max_amount = cnt
                cnt = keyboards[i]
                print(keyboards[i], drives[j], max_amount)
            cnt = keyboards[i]
    if max_amount == 0:
        return -1
    else:
        return max_amount

b = 10
n = 2
m = 3
keyboards = [3, 1]
drives = [5, 2, 8]

result = getMoneySpent(keyboards, drives, b)
print(result)