# 배열 A, B에서 각각 한 개의 숫자를 뽑아 두 수를 곱합니다. 이러한 과정을 배열의 길이만큼 반복하며, 
# 두 수를 곱한 값을 누적하여 더합니다. 이때 최종적으로 누적된 값이 최소가 되도록 만드는 것이 목표입니다.

def solution(A,B):
    answer = 0
    A = sorted(A)
    B = sorted(B, reverse=True)
   
    for i in range(len(A)):
        answer = answer + (A[i] * B[i])
        
    return answer

# 누적값을 최소로 만들기  위해  A의 가장 작은 수와 B의 가장 큰 수를 곱하여 최대한 최소의 수를 출력하도록 한다. 