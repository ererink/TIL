import sys
sys.stdin = open("input.txt")

"""
11
449047 855428 425117 532416 358612 929816 313459 311433 472478 589139 568205 
7
I 1 5 400905 139831 966064 336948 119288 
I 8 6 436704 702451 762737 557561 810021 771706 
I 3 8 389953 706628 552108 238749 661021 498160 493414 377808 
I 13 4 237017 301569 243869 252994 
I 3 4 408347 618608 822798 370982 
I 8 2 424216 356268 
I 4 10 512816 992679 693002 835918 768525 949227 628969 521945 839380 479976 
"""

T = 10
# ctrl + d
# 원본암호문 = [449047,855428,425117,532416,358612,929816,313459,311433,472478,589139,568205]

for t in range(1, T+1):
    origin_len = int(input())
    origin_list = list(map(int, input().split()))

    command_len = int(input())
    command_list = input().split()

    # i의 초기화
    i = 0
    
    # while문 (반복문)
    while i < len(command_list):
        command = command_list[i]
        if command == "I":
            # x,y,숫자리스트 s 구해야한다.
            x = int(command_list[i+1])
            y = int(command_list[i+2])
            # print(type(y))
            number_list = command_list[i+3 : i+3+y]

            # insert 메서드를 써서 x의 위치에 숫자들을 삽입한다.
            # 역순으로 삽입한다.
            for number in number_list[::-1]:
                origin_list.insert(x, int(number))

        # 0 + 1 -> 1
        i = i + 1
    

    # print(origin_list[:10])
    print(f"#{t}",*origin_list[:10])