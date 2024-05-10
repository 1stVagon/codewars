def remove_smallest(numbers):
    new_array = numbers.copy()
    if len(new_array) > 0:
        new_array.remove(min(new_array))
        return new_array
    else:
        return []