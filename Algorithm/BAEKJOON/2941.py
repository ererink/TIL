# 크로아티아 알파벳

alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in alphabet :
    word = word.replace(i, '!')

print(len(word))