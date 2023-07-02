def solution(sizes):
    answer = 0
    n = len(sizes)
    
    for i in range(n):
        # 모두 한 방향으로 명함 정렬
        sizes[i] = sorted(sizes[i])
    
    max_w = 0
    max_h = 0
    # 최댓값 구하기
    for i in range(n):
        if max_w < sizes[i][0]:
            max_w = sizes[i][0]
        if max_h < sizes[i][1]:
            max_h = sizes[i][1]
    
    answer = max_w * max_h
    return answer
