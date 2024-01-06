from functools import reduce


def amount_payment(payment):
    return reduce((lambda x, y: x + y if y >= 0 else x ), payment, 0)