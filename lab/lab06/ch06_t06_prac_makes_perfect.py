def cube(number):
    number = number ** 3


def by_three():
    if number % 3 == 0:
        return cube(number)
    else:
        return False


by_three(6)
