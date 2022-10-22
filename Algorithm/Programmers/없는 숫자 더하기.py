def solution(numbers):
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    answer = 0
    
    for i in nums:
        if i in numbers:
            continue
        else:
            answer += i
    return answer