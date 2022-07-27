# https://school.programmers.co.kr/learn/courses/30/lessons/68644

def solution(numbers):
    answer = []
    n = len(numbers)    # numbers의 개수를 n에 넣는다. 
    for i in range(n):  # n==5, 0-4를 i에 넣는다. 
        for j in range(i + 1, n):   # 현재 i보다 큰 값이 되어 다른 위치의 인덱스 값을 더해준다. 
                                    # i보다 들여써져 있기 때문에 j값이i i보다 먼저 더해지며 인덱스 위치를 바꾼다.
            answer.append(numbers[i] + numbers[j]) # 서로 다른 위치의 인덱스 값을 계속해서 더해주며, 
                                                   # answer 리스트에 더해준 값을 넣는다. 
    answer = set(answer)    # answer 리스트의 중복 제거
    return sorted(answer)   # answer 리스트의 정렬

print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))