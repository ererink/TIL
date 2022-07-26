# 아래 코드는 문자열을 입력받아 단어별로 나누는 코드이다.

# 오류 코드
words = list(map(int, input().split()))
print(words)

# 해결 코드
words = list(map(str, input().split()))
print(words)