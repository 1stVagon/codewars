def filter_list(l):
    list = []
    for el in l:
        if isinstance(el, str) == False:
            list.append(el)
    return list