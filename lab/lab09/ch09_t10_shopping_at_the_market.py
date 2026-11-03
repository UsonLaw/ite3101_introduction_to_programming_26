def compute_bill(food):
    total = 0
    for item in food:
        total += price[item]    return total