from decimal import Decimal, getcontext


def decimal_average(number_list, signs_count):
    getcontext().prec = signs_count + 2
    numbers = [Decimal(number) for number in number_list]
    avg = Decimal(sum(numbers) / len(numbers))
    avg_final = round(avg, 3)
    print(avg)
    return avg

# Приклад використання:
# number_list = [4.5788689699797, 34.7576578697964, 86.8877666656633, 12]
number_list = [4, 15, 1.77, 23, 1.33543546, 7, 89]

signs_count = 6

average = decimal_average(number_list, signs_count)
print(average)
