# 민석이는 불면증에 걸렸다. 그래서 잠이 안 올 때의 민간요법 중 하나인 양 세기를 하려고 한다.
# 민석이는 1번 양부터 순서대로 세는 것이 재미없을 것 같아서 N의 배수 번호인 양을 세기로 하였다.
# 즉, 첫 번째에는 N번 양을 세고, 두 번째에는 2N번 양, … , k번째에는 kN번 양을 센다.
# 이렇게 숫자를 세던 민석이에게 잠은 더 오지 않고 다음과 같은 궁금증이 생겼다.
# 이전에 셌던 번호들의 각 자리수에서 0에서 9까지의 모든 숫자를 보는 것은 최소 몇 번 양을 센 시점일까?

t = int(input())
for test_case in range(1, t + 1):
    
    n = int(input())
    cnt = []
    # (1~9) * N 의 값을 변수에 넣는다. 될 때 까지 == 반복문
    for i in range(1, 11):
        num = n * i
        cnt = list(map(int, str(num)))
        cnt.append(cnt)
        # 계산된 배수의 값이 0~9 다 모이면 중단한다. 
        if cnt == list(range(0, 10)) : 
            break
    print(i)

# i(1~9) * N 값을 변수에 넣는다.
# 그 변수는 문자열로 바꿔 분할해준다.
# 값들을 리스트에 담는다. 
# 0~9까지 숫자가 다 담기면 k를 출력한다. 

t = int(input())
for test_case in range(1, t + 1):

    n = int(input())


# 모범 답안
# 숫자 -> 문자 -> 숫자 
# 모든 수(0~9)가 체크될 때 까지 반복한다 == while문 
# 모든 수의 체크 방법은 
# 1. 리스트에 0이 없을 때 까지 
# 2. 중복제거 (set()) set의 길이가 10이 될 때 까지 (알아서 중복 제거가 되니까)
# 정수를 문자열로 분할한다. 

# set() 풀이 
t = int(input())
for test_case in range(1, t + 1):
    N = int(input())
    N1 = N 
    numbers = set() # 기록지 
    # while 반복 => set 길이가 10이 될 때 까지 
    while True:
        # for 반복: 숫자를 문자로 변환 
        for n in str(N):
            # numbers set에 추가 
            numbers.add(n)
        if len(numbers) == 10:
            break
        # print(n, numbers)
        N += N1
    print(f'#{test_case} {N}')