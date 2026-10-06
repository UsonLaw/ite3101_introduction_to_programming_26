def cube(number):
    number = number ** 3


def by_three(number):
    if number % 3 == 0:
        return cube(number)
    else:
        return False


by_three(7)
