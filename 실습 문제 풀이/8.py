# 8번 두번째로 큰 수 구하기
# 주어진 리스트 numbers에서 두번째로 큰 수를 구하여 출력하시오.
# max() 함수 사용 금지

numbers = [0, 20, 100]

numbers.sort(reverse = True) #오름차순으로 정렬한 뒤 두번째 인덱스 값을 출력한다.
print(numbers[1])