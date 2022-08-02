# 자료구조는 정말 최고야


N, M = map(int, input().split())

for test_case in range(M):
    M_info = int(input())
    books = list(map(int, input().split()))

    for i in books:
        if books[i] > books[i+1]: # IndexError: list index out of range
            books = books.pop()
            break

        else:
            continue           # 아니면 걍 넘어가

if books.isEmpty() == True:
    print('YES')

else:
    print('NO')
 

# 정렬되어 있는지 확인하는 것 
# 리스트에 있는 값을 pop한 값과 맨 위의 값을 비교하며 pop한다. 
# 스택이 비워질 때 까지 반복한다.

stack_list = [[12, 4, 1], [6, 2], [9, 3, 7], [11, 10, 8, 5]]

answer = 'YES'                                                  # 대답의 기본값은 'YES'로 가정하는 것이다


for stack in stack_list:                                        # stack에는 하나의 리스트 단위로 들어온다
    comparison = stack.pop()                                    # pop으로 꺼낸다

    while len(stack) != 0:                                      # 스택이 비어있지 않을 때 까지 반복한다. 

        # 맨 위의 값과 비교한다.
        if stack[-1] > comparison:
            comparison = stack.pop()                            # pop dmf tkdydgotj comparison 값을 갱신한다

        else:
            answer = 'NO'
            break
    print(answer)