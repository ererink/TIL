# 패턴 마디의 길이

t = int(input())
for test_case in range(1, t + 1):
    pattern = input()
    cnt = 0

    for i in range(1, 30):
        if pattern[i] == pattern[0]:
            if pattern[:i] == pattern[i:i * 2]:
                cnt = i
                break

        
    print("#{} {}".format(test_case, cnt))