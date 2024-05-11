def remove_char(s):
    sList = []
    for i in s:
        sList.append(i)
    sList.remove(sList[0])
    sList.remove(sList[-1])
    return ''.join(sList)