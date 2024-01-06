from random import randrange

def get_numbers_ticket(min_val, max_val, quantity):
    # Перевіряємо умови обмежень на параметри функції
    if min_val < 1 or max_val > 1000 or min_val >= quantity or quantity >= max_val:
        return []

    # Генеруємо та повертаємо випадковий набір чисел без дублікатів
    return sorted([randrange(min_val, max_val) for _ in range(quantity)])

# Приклад використання:
min_val = 1
max_val = 49
quantity = 6
result = get_numbers_ticket(min_val, max_val, quantity)
print(result)
