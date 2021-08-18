

def isValid(s):
    dictForParentheses = {
    ")" : "(",
    "]" : "[",
    "}" : "{"
    }
    stack = []
    openingTagsRef = ['(', '[', '{']
    for i in s:
        if len(stack) == 0:
            stack.append(i)
        else:
            if i not in openingTagsRef and stack[len(stack) - 1] == dictForParentheses[i]:
                stack.pop(len(stack) - 1)
            else:
                stack.append(i)
    return len(stack) == 0

isValid("(()[])")