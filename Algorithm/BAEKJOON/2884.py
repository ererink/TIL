# 알람 시계
'''
원래 설정되어 있는 알람을 45분 앞서는 시간으로 바꾸는 것이다. 
어차피 알람 소리를 들으면, 알람을 끄고 조금 더 잘 것이기 때문이다. 이 방법을 사용하면, 매일 아침 더 잤다는 기분을 느낄 수 있고, 학교도 지각하지 않게 된다.

10 10
'''

hour, minute = map(int, input().split())

if minute < 45 :	    # 분단위가 45분보다 작을 때 
    if hour == 0 :	    # 0 시이면
        hour = 23
        minute += 60
    else :	            # 0시가 아니면 (0시보다 크면)
        hour -= 1	
        minute += 60
        
print(hour, minute - 45)	
