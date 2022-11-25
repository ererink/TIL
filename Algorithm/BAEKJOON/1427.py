'''
소트인사이드
'''

N = map(int, input())
N = sorted(N, reverse=True)


result = "".join(N)
print(result)

a = input()

lis=[]
lis2=[]

lis.append(a)
for i in lis:
    for j in i:
        lis2.append(j)

lis2.sort(reverse=True)
b = "".join(lis2) 
print(b)