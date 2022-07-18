# 숫자의 길이 구하기
# 양의 정수number를 문자열로 변경하는 것은 금지입니다. str() 사용 금지

def digit_cnt(n):
    cnt = 0
    while n:
        n //= 10
        cnt += 1
    return cnt

print(digit_cnt(123))

# 10으로 나누어 몫을 활용한다. 
# while문을 통해 몫이 0이 되는 순간까지 자릿수를 증가시킨다. 
# 입력값을 10으로 나눠가며 나머지를 버리고 몫만 남길 때마다 cnt에 1씩 증가시킨다. 
# while문을 탈출할 때는 0이 되고 cnt에는 숫자의 길이가 담긴다.