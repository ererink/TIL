# 단어 공부

word = input().upper()                                  # 대문자로 입력값을 받는다
chr_list = list(set(word))                              # for문을 위해 중복값을 제거한 입력값의 문자열 하나씩 리스트에 저장한다

chr_cnt = []                                            # 중복된 문자열의 카운트 값을 저장
for i in chr_list:                                      # 중복 제거한 문자열 수 만큼 반복
    chr_cnt.append(word.count(i))                       # i에 있는 문자열과 동일한 word(입력값)의 문자열 개수를 chr_cnt에 넣어준다. (정수) (중복 문자열 개수 저장)

if chr_cnt.count(max(chr_cnt)) > 1:                     # 만약 중복된 개수 중 제일 큰 수가 1개 이상 있다면
    print('?')                                          # '?'를 출력한다
else:                                                   # 그렇지 않을 시 
    print(chr_list[(chr_cnt.index(max(chr_cnt)))])      # 중복 문자열 개수(chr_cnt)의 큰 수(max)를 찾아서(index) 해당되는 문자열을(chr_list에서) 출력한다. 