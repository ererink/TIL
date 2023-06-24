def solution(sizes):
    answer = 0
    result = []
    n = len(sizes)
    
    max_w = 0
    max_h = 0
    # 바꾸지 않고 큰 수 구하기
    for i in range(n):
        # 큰 수 구하기
        if max_w < sizes[i][0]:
            max_w = sizes[i][0]
        if max_h < sizes[i][1]:
            max_h = sizes[i][1]
            
    result.append(max_w * max_h)
    
    
    for i in range(n):
        # 바꾸기
        temp = sizes[i][0]
        sizes[i][0] = sizes[i][1]
        sizes[i][1] = temp
        
        max_w = 0
        max_h = 0
        # 0부터 다시 스캔
        for j in range(n):
            # 최댓값 구하기
            if max_w < sizes[j][0]:
                max_w = sizes[j][0]
            if max_h < sizes[j][1]:
                max_h = sizes[j][1]
        
        # 복구
        temp = sizes[i][0]
        sizes[i][0] = sizes[i][1]
        sizes[i][1] = temp
        
        print(max_w, max_h)
        result.append(max_w * max_h)
    
    answer = min(result)
    return answer
