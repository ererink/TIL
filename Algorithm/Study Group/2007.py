# SWEA 패턴 마디의 길이

t = int(input())
for test_case in range(1, t + 1):
    pattern = input()
    cnt = 0                                         # 출력값의 길이 측정

    for i in range(1, 30):                          # 입력값은 최대 30이므로 범위를 30으로 설정한다. 
                                                    # pattern[0]의 값과 비교해야 하므로 범위를 1부터 설정한다. 
        if pattern[i] == pattern[0]:                # pattern[1]의 값부터 입력값의 첫번째 값과 비교하여 같은 값을 찾는다. 
                                                    # 해당 비교값이 같은 경우
            if pattern[:i] == pattern[i:i * 2]:     # pattern[0]-pattern[i]까지의 값이 다음 패턴도 같은 단어인지 확인한다.
                cnt = i                             # 해당 조건이 맞다면 i는 패턴(단어)의 문자열 길이와 같다.
                break

        
    print("#{} {}".format(test_case, cnt))