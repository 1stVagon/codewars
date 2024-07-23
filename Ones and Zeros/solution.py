def binary_array_to_number(arr):
    string = ''
    for el in arr:
        string += str(el)
    return(int(string, 2))
