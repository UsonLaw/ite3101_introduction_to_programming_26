def median(numbers):
    sorted_list = sorted(numbers)
    length = len(sorted_list)
    mid = length // 2
    if length % 2 == 0:
        return (sorted_list[mid - 1] + sorted_list[mid]) / 2.0
    else:
        return sorted_list[mid]