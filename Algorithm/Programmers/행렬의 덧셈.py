def solution(arr1, arr2):    
    answer = []

    for i in range(len(arr1)):
        tem = []
        for j in range(len(arr1[0])):
            tem.append(arr1[i][j] + arr2[i][j])
        answer.append(tem)
            
    return answer