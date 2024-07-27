def solution(a, b):
    short = ''
    long = ''
    
    if len(a) < len(b):
        short = a
        long = b
    else:
        short = b
        long = a
    
    return short + long + short