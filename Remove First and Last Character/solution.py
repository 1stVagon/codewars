def remove_char(s):
    sList = []
    for i in s:
        sList.append(i)
    sList.pop(0)
    sList.pop()
    return ''.join(sList)