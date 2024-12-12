def solution(s):
    result = []
    word = ''
    for char in s:
        if char.isupper() and word:
            result.append(word)
            word = ''
        word += char
    result.append(word)
    print(' '.join(result))

solution('helloWorld')