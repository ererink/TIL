def missingNumbers(arr, brr):
    arr_cnt = {}
    brr_cnt = {}
    answer = []
    temp_set = list(set(brr))
    for i in temp_set:
        brr_cnt[i] = brr.count(i)
        arr_cnt[i] = arr.count(i)
    
    for i in arr_cnt:
        if arr_cnt[i] < brr_cnt[i] or arr_cnt[i] == 0:
            answer.append(i)
    return answer
arr = [203, 204, 205, 206, 207, 208, 203, 204, 205, 206]
brr = [203, 204, 204, 205, 206, 207, 205, 208, 203, 206, 205, 206, 204]

# arr = [7, 2, 5, 3, 5, 3]
# brr = [7, 2, 5, 4, 6, 3, 5, 3]
answer = missingNumbers(arr, brr)
print(answer)