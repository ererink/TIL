# 뒤집힌 덧셈

a, b = input().split()              # str으로 입력값 받기

sum_ = int(a[::-1]) + int(b[::-1])  # a, b(입력값)을 역순으로 뒤집고([::-1]), int로 바꿔주고
                                    # 바뀐 정수값을 더해서 sum_ 변수에 넣는다.

result = str(sum_)                  # 더한 값(sum_)을 문자열로 바꿔 result에 넣는다. 
                                    # 결과값을 역순으로 출력하기 위해 다시 문자열로 바꾼다.

print(int(result[::-1]))            # result를 역순으로 출력하며 동시에 정수로 출력한다.

# 형 변환: str -> 합산:int -> str -> 출력: int 