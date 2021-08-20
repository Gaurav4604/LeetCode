def addBinary(a:str, b:str):
    if len(a) < len(b):
        smaller = list(map(int, list(a)))
        larger = list(map(int, list(b)))
    else:
        smaller = list(map(int, list(b)))
        larger = list(map(int, list(a)))

    while (len(smaller) != len(larger)):
        smaller.insert(0, 0)
    
    carry = 0
    ls = []

    for i in reversed(range(len(larger))):
        if bool(smaller[i] & larger[i]):
            ls.append(carry)
            carry = 1
        elif bool(smaller[i] | larger[i]):
            if carry & 1:
                ls.append(0)
                carry = 1
            else:
                ls.append(1)
                carry = 0
        else:
            ls.append(carry)
            carry = 0
    if carry == 1:
        ls.append(carry)

    return "".join(list(map(str, ls[::-1])))

addBinary("1101", "101")