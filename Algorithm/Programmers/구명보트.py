def solution(people, limit):
    answer = 0
    start = 0
    end = len(people) - 1
    people = sorted(people)
    
    while start <= end:
        if start == end:
            answer += 1
            break
            
        # 큰 사람만 빼기
        if people[start] + people[end] > limit:
            answer += 1
            end -= 1
        # 두 사람 다 빼기
        elif people[start] + people[end] <= limit:
            answer += 1
            start += 1
            end -= 1
        

    return answer