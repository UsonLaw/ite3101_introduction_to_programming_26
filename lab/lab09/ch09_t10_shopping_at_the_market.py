def compute_bill(food: List[str]) -> float:
    total = 0
    for item in food:
        total += prices[item]
    return total