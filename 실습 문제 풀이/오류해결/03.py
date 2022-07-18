# 두 수를 Input으로 받아 합을 구하는 코드이다.

# 오류 코드
numbers = input().split()
print(sum(numbers))

# 오류 해결 코드
numbers = map(int,input().split())
print(sum(numbers))