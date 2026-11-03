def compute_bill(food):
    total = 0
    for key in food:
        total += [key] * food[key]
    return total