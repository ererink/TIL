def solution(phone_book):
    answer = True
    for i in range(len(phone_book)):
        for j in range(i + 1, len(phone_book)):
            if phone_book[i].startswith(phone_book[j]):         # 시작값이 같은 것을 찾는다
                answer = False
            if phone_book[j].startswith(phone_book[i]):
                answer = False
    return answer

