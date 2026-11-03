def compute_bill(food):
    total = 0
    for key in food:
        total += food[key]
    return total