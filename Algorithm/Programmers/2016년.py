import datetime
def solution(a, b):
    answer = ''
    
    date = datetime.datetime(2016, a, b, 0, 0)
    day = date.weekday()
    
    if day == 0:
        answer = "MON"
    elif day == 1:
        answer = "TUE"
    elif day == 2:
        answer = "WED"
    elif day == 3:
        answer = "THU"
    elif day == 4:
        answer = "FRI"
    elif day == 5:
        answer = "SAT"
    else:
        answer = "SUN"
        
    return answer