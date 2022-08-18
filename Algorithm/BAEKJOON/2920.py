# 음계

from posixpath import split


major = list(map(int, input().split()))


if [1, 2, 3, 4, 5, 6, 7, 8] == major:
    print('ascending')

elif [8, 7, 6, 5, 4, 3, 2, 1] == major:
    print('descending')

else:
    print('mixed')
