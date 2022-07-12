# 8번 두번째로 큰 수 구하기
# 주어진 리스트 numbers에서 두번째로 큰 수를 구하여 출력하시오.
# max() 함수 사용 금지

numbers = [0, 20, 100]

numbers.sort(reverse = True) #오름차순으로 정렬한 뒤 두번째 인덱스 값을 출력한다.
print(numbers[1])

# sort() 안쓴.ver

numbers = [0, 20, 100, 40]
max_number = numbers[0]
second_number = numbers[0]

# 1. 전체 숫자를 반복
for n in numbers:
    # 만약에 n이 최대보다 크다면
    if max_number < n:
        # 최대값이었던 것이 두번째로 큰 수가 된다. 
        second_number = max_number # 과거 최대값을 second_number에 넘겨준다.
        max_number = n # n값을 현재 최대값으로 넘겨준다. 
    elif second_number < n and n < max_number:
        second_number = n

print(second_number)


