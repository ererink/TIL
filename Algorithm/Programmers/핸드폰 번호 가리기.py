def solution(phone_number):
    answer = ''
    ph_len = len(phone_number)
    answer = '*' * (ph_len - 4)     # 뒷번호 4자리를 뺀 수만큼 '*'을 할당
    answer += phone_number[-4:]     # 입력값 뒤 4자리만 할당
    return answer