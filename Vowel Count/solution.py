def get_count(sentence):
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    sentence = ''.join(sentence)
    for i in sentence:
        for j in vowels: 
            count += 1 if i == j else 0
    return count