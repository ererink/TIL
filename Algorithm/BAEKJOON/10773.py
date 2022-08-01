# stack
# 제로

# 0이면 가장 최신값 삭제
# 0이 아니면 계속 입력 
'''
4 -> 입력 개수
3
0
4
0
'''

K = int(input())

input_list = []

for _ in range(K):
    input_list.append(int(input())) 

stack = []

for elem in input_list:
    if elem != 0:
        stack.append(elem)
    else:
        stack.pop

print(sum(stack))