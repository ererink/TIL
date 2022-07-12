# 6번 최댓값 구하기
# 주어진 리스트 numbers에서 최댓값을 구하여 출력하시오.
# max() 함수 사용 금지

numbers = [0, 20, 100]
maximum = numbers[0] # maximum = 0 도 가능하다.

for i in numbers:
  if i > maximum:
    maximum = i # i가 더 크다면 최대값을 i의 값으로 바꿔준다. (계속 반복)
                # 이 과정을 거친다면 당연히 최대값을 찾게된다. 

print(maximum)

numbers = [-10, -100, -30] # 예시 값이 모두 음수일 때
maximum = numbers[0] # 0으로 설정해둔다면 리스트의 값보다 다 작기 때문에 실행되지 않는다.
                     # 대신 첫 번째 값을 비교값으로 초기화한다면 for문 실행이 가능하다.

for i in numbers:
  if i > maximum:
    maximum = i # i가 더 크다면 최대값을 i의 값으로 바꿔준다. (계속 반복)
                # 이 과정을 거친다면 당연히 최대값을 찾게된다. 

print(maximum)