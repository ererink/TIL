# 대칭 차집합
# 자연수를 원소로 갖는 공집합이 아닌 두 집합 A와 B가 있다. 
# 이때, 두 집합의 대칭 차집합의 원소의 개수를 출력하는 프로그램을 작성하시오.

A, B = map(int, input().split())
A_input = set(map(int, input().split()))    # set 키워드를 사용한다.
B_input = set(map(int, input().split()))

diff1 = []
diff2 = []

diff1 = A_input.difference(B_input)
diff2 = B_input - A_input

print(len(diff1) + len(diff2))