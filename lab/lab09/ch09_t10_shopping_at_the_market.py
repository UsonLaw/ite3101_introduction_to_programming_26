def compute_bill(food):
    total = 0
    for key in food:
        total += prices[key] * food[key]
    return total