'''
26 5        => 포켓몬 개수, 맞춰야하는 문제의 개수
Bulbasaur
Ivysaur
Venusaur
Charmander
Charmeleon
Charizard
Squirtle
Wartortle
Blastoise
Caterpie
Metapod
Butterfree
Weedle
Kakuna
Beedrill
Pidgey
Pidgeotto
Pidgeot
Rattata
Raticate
Spearow
Fearow
Ekans
Arbok
Pikachu
Raichu      => 여기까지 도감 (26번째)
25
Raichu
3
Pidgey
Kakuna

output =  Pikachu
            26
            Venusaur
            16
            14

- 딕셔너리 사용
'''

n, m = map(int, input().split())

poket_dict1 = {}    # key = int
poket_dict2 = {}    # key = str

for i in range(1, n+1):
    name = input()
    poket_dict1[str(i)] = name
    poket_dict2[name] = str(i)

for j in range(m):
    check = input() # 정수, 문자열 모두 문자열로 받는다

    if check.isdigit():         # input이 정수일 때
        answer = poket_dict1[check] # value 찾기
        print(answer)
    
    else:                       # input이 문자열일 때
        answer = poket_dict2[check] 
        print(answer)
