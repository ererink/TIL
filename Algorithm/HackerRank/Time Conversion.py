def timeConversion(s):
    temp = ''
    if s[-2:] == 'PM':
        if s[:2] == '12':
            temp += s[:2]
        else:
            temp = str(12 + int(s[:2]))
        
    else:
        if s[:2] == '12':
            temp += '00'
        else:
            temp += s[:2]

    return(temp + s[2:-2])

s = '12:45:54PM'
check = timeConversion(s)
print(check)