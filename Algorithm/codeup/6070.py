# 월이 입력될 때 계절 이름이 출력되도록 해보자.

# 월 : 계절 이름
# 12, 1, 2 : winter
  # 3, 4, 5 : spring
  # 6, 7, 8 : summer
  # 9, 10, 11 : fall

m = int(input())

if (m == 12 or m == 1 or m == 2):
    print('winter')

elif (m == 3 or m == 4 or m == 5):
    print('spring')

elif (m == 6 or m == 7 or m == 8):
    print('summer')

else:
    print('fall')