def migratoryBirds(arr):
    arr = sorted(arr)
    max_bird = 0
    max_cnt = 0
    for i in set(arr):
        cnt = arr.count(i)
        if cnt > max_cnt:
            max_cnt = cnt
            max_bird = i  
        elif cnt == max_cnt:
            if i < max_bird:
                max_bird = i
                
    return max_bird