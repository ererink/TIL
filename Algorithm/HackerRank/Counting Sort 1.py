def countingSort(arr):
    answer = [0] * 100
    
    for i in arr:
        answer[i] += 1
        
    return answer    