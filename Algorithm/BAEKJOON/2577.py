# 숫자의 개수
# 세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.


# 방법 1
a = int(input())
b = int(input())
c = int(input())
result = list(str(a * b * c)) #a*b*c의 값을 문자열로 변환한 리스트를 result에 넣어준다. 

for i in range(10): #0-9까지 i에 넣어준다. 
    print(result.count(str(i)))

