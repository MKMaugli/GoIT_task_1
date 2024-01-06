def encode(data):
    if not data:
        return []

    result = []
    count = 1

    # Перевіряємо, чи поточний елемент співпадає з наступним
    while count < len(data) and data[count] == data[0]:
        count += 1

    # Додаємо елемент та кількість до результату
    result.extend([data[0], count])

    # Рекурсивно викликаємо функцію для решти списку
    result.extend(encode(data[count:]))

    return result

# Приклад використання:
original_string = "XXXXXZXYYYYZZ"
encoded_result_string = encode(list(original_string))
print(encoded_result_string)
