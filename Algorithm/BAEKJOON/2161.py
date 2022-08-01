# N장의 카드가 있다. 각각의 카드는 차례로 1부터 N까지의 번호가 붙어 있으며, 
# 1번 카드가 제일 위에, N번 카드가 제일 아래인 상태로 순서대로 카드가 놓여 있다.

# 이제 다음과 같은 동작을 카드가 한 장 남을 때까지 반복하게 된다. 
# 우선, 제일 위에 있는 카드를 바닥에 버린다. 
# 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.
# 첫째 줄에 버리는 카드들을 순서대로 출력한다. 제일 마지막에는 남게 되는 카드의 번호를 출력한다.


from collections import deque

n = int(input())
nums = deque(list(range(1, n + 1)))

while len(nums) > 1:
    print(nums.popleft(), end=" ")
    nums.append(nums.popleft())


print(nums[0])