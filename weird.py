def StrangeFunc(stringInput):
    result = []
    for i, char in enumerate(stringInput):
        if i % 2 == 0:
            result.append(chr(ord(char) - i))
        else:
            result.append(chr(ord(char) + i))
    return ''.join(result)

key = 'lbwhn=u^AW#V9eo'
print(StrangeFunc(key))
