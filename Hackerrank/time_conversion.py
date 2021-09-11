def timeConversion(s:str):
    ls = s.split(':')

    if ls[2][2:] == 'PM' and int(ls[0]) != 12:
        ls[0] = str(int(ls[0]) + 12)

    elif ls[2][2:] == 'AM' and ls[0] == '12':
        ls[0] = '00'
    
    ls[2] = ls[2][:2]

    return ":".join(ls)

print(timeConversion('11:01:00PM'))