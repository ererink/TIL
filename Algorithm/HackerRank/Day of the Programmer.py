def dayOfProgrammer(year):
    if year < 1918:
        # Yoon
        if year % 4 == 0:
            answer = '12.09.' + str(year)
            return answer
        else:
            answer = '13.09.' + str(year)
            return answer
    
    elif year > 1918:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            answer = '12.09.' + str(year)
            return answer
        else:
            answer = '13.09.' + str(year)
            return answer
    
    else:
        answer = '26.09.' + str(year)
        return answer