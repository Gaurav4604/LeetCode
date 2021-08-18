class RomanNumber:
    def __init__(self, data, priority, value):
        self.data = data
        self.priority = priority
        self.value = value

romanNumsList = [
    RomanNumber("I", 0, 1),
    RomanNumber("V", 1, 5),
    RomanNumber("X", 2, 10),
    RomanNumber("L", 3, 50),
    RomanNumber("C", 4, 100),
    RomanNumber("D", 5, 500),
    RomanNumber("M", 6, 1000),
]

def individualConverter(romData):
    for i in romanNumsList:
        if i.data == romData:
            return i

def romanToInt(romanNumber):
    total = 0
    prevPriority = 0
    listForNumber = []
    for i in romanNumber:
        listForNumber.append(individualConverter(i))
    for i in reversed(range(len(listForNumber))):
        if (i == len(listForNumber) - 1):
            prevPriority = listForNumber[i].priority
            total += listForNumber[i].value
        else:
            if prevPriority <= listForNumber[i].priority:
                total+= listForNumber[i].value
            else:
                total-= listForNumber[i].value
            
            prevPriority = listForNumber[i].priority
    return total

print(romanToInt("MCMXCIV"))