import itertools

# 소수 확인 함수
def prime_n(n):
    if n == 0 or n == 1:
        return False
    else:
        for i in range(2, (n // 2) + 1):
            if n % i == 0:
                return False
        return True

def solution(nums):
    answer = 0
    # 3개의 수 조합
    triple = list(itertools.combinations(nums, 3))
    for j in triple:
        if prime_n(sum(j)):
            answer += 1

    return answer