def solution(arr):
    answer = []
    n = len(arr)
    answer.append(arr[0])
    for i in range(1, n):
        if arr[i] != arr[i-1]:
            answer.append(arr[i])
    return answer