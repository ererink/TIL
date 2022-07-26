# 정수 2개(a, b)를 입력받아 a에서 b를 뺀 차를 출력하는 프로그램을 작성해보자.

# 방법 1
a, b = input().split()
c = int(a)-int(b)

print(c)

# 방법 2
a, b = map(int, input().split()) # 방법 1의 c 변수로 int를 여러번 적어야 할 것을 
                                 # map으로 묶어서 한꺼번에 전부 int으로 바꿀 수 있다. 
                                 # 이는 코드를 줄이고 가독성을 높인다. 
                                 # .split은 값 입력 시 한줄에서 받기 위함이다. (스페이스 사용)

print(a-b)