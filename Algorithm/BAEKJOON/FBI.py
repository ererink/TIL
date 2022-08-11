fbi = []
for i in range(5):
    fbi.append(input())

check = 0
for j in range(len(fbi)):
    if 'FBI' in fbi[j]:
        print(j + 1, end=" ")
        check = 1

if check == 0:
    print('HE GOT AWAY!')
