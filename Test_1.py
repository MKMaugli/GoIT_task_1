def is_integer(s):
    # Перевірка на пустий рядок
    if len(s) == 0:
        return False

    # Видалення початкових і кінцевих прогалин
    s = s.strip()

    # Перевірка на наявність символів після видалення прогалин
    if len(s) == 0:
        return False

    # Перевірка на цілі числа
    try:
        int(s)
        return True
    except ValueError:
        return False

# Приклад використання:
result = is_integer("  +123  ")
print(result)  # Виведе True
