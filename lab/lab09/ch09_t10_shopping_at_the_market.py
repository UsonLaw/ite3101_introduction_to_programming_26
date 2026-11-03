def compute_bill(food):
    total = 0
    for item in food:
        total += prices[item]    
    return total