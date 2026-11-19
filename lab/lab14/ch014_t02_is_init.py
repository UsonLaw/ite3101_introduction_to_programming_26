def is_int(x):
    if abs(x - round(x)) == 0:
        return True
    else:
        return False