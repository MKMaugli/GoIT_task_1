def factorial(n):
    if n < 2:
        return 1  # Базовый случай
    else:
        return n * factorial(n - 1)  # Рекурсивный случай


# num = int(input("Введите положительное целое число: "))
# result = factorial(num)
# print(f"Факториал числа {num} равен {result}")

def number_of_groups(n, k):
    result_count = int(factorial(n) / (factorial(n - k) * (factorial(k))))
    return result_count

print(number_of_groups (50, 7))