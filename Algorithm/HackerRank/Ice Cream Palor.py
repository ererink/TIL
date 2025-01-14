# 브루트포스
def icecreamParlor(m, arr):
    max_amount = 0
    answer = []
    for i in range(n):
        cnt = arr[i]
        for j in range(i + 1, n):
            if cnt + arr[j] <= m:
                cnt += arr[j]
            
                if max_amount <= cnt:
                    max_amount = cnt
                    answer = [i + 1]
                    answer.append(j + 1)
                
            cnt = arr[i]
    return answer
arr = [1, 4, 5, 3, 2]
n = len(arr)