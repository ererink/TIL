# 한수

num = int(input())

hansu = 0
for i in range(1, num+1):
    num_list = list(map(int, str(i)))
    if i < 100:
        hansu += 1  # 100보다 작으면 모두 한수
    elif num_list[0]-num_list[1] == num_list[1]-num_list[2]:
        hansu += 1  # x의 각 자리가 등차수열이면 한수
print(hansu)

# 두 자리 숫자는 등차수열인지 비교대상이 없기 때문에 모두 한수이고 세자리 숫자는 각 자리의 숫자 간격이 동일하면 한수이다. 
# 1~99는 모두 한수이다. 그래서 if 조건식으로 변수i가변수 i가 100보다 작은 경우 모두 hansu라는 변수에 숫자를 더하도록 했고 
# 변수 i가 100 이상인 경우 3자리 숫자를 앞의 두 자리의 차이와 뒤의 두 자리의 차이가 같으면 한수이다.