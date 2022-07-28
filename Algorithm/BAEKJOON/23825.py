# SASA 모형을 만들어보자

n, m = map(int, input().split())    
result = []                         # S와 A를 만들 수 있는 개수 각자 저장할 공간
result = n //2, m//2                # S와 A는 2개씩 있어야 1개를 만들 수 있으므로
                                    # 2를 나눈 몫을 계산하여 result 리스트에 결과값을 저장한다

print(min(result))                  # 결국 S와 A의 개수가 맞아야 하므로 최솟값을 출력한다. 