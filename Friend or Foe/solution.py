def friend(x):
    names = []
    for name in x:
        if len(name) == 4:
            x.append(name)
    return names