def breakingRecords(scores):
    max_score = scores[0]
    min_score = scores[0]
    max_cnt, min_cnt = 0, 0
    
    for i in range(1, len(scores)):
        if scores[i] > max_score:
            max_score = scores[i]
            max_cnt += 1
        elif scores[i] < min_score:
            min_score = scores[i]
            min_cnt += 1
    
    return [max_cnt, min_cnt]
