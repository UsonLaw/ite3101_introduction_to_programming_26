def count(sequence, item):
    total = 0
    for elem in sequence:
        if elem == item:
            total += 1
    return total