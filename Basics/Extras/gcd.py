def gcd(x, y):
    a = x
    b = y
    if (b == 0):
        return a
    else:
        while b != 0:
            c = a % b
            print(f'{a} {b} {c}')
            a = b
            b = c
        return a
    
print(gcd(1970, 1066))