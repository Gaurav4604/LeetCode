def plus_one(digits:list):
    digits = digits[::-1]
    for i in range(len(digits)):
        if digits[i] != 9:
            digits[i] += 1
            return digits[::-1]
        else:
            digits[i] = 0
    digits.append(1)
    return digits[::-1]


print(plus_one([8, 7, 9, 9]))