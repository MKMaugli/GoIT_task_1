def prepare_data(data):
    if len(data) < 2:
        # Якщо у списку менше двох елементів, немає необхідності видаляти екстремальні значення.
        return data
    
    # Видалення найбільшого та найменшого значень.
    data.remove(max(data))
    data.remove(min(data))
    
    # Сортування списку в порядку зростання.
    sorted_data = sorted(data)
    
    return sorted_data

# Приклад використання:
input_data = [4, 7, 2, 10, 5, 1]
result = prepare_data(input_data)
print("Змінений список:", result)
