from operator import and_
from functools import reduce

def longestCommonPrefix(ListOfWords:list):
    ListOfWordsAlphabets = [list(i) for i in ListOfWords]
    minLengthWords = min([len(list(i)) for i in ListOfWords])
    mainSubSequence = ""
    for i in range(minLengthWords):
        flag = False
        letter = ListOfWordsAlphabets[0][i]
        for j in ListOfWordsAlphabets[1:]:
            if not letter == j[i]:
                flag = True
                break
        if flag:
            break
        else:
            mainSubSequence += letter
    return mainSubSequence


print(longestCommonPrefix(["aa","ab"]))