import base64

def encode_data_to_base64(data):
    # Створення нового списку для збереження закодованих пар username:password
    encoded_list = []

    # Ітерація по кожному елементу у вхідному списку
    for item in data:
        # Розділення пари username:password
        username, password = item.split(':')

        # Кодування пари у форматі Base64
        encoded_pair = base64.b64encode(f"{username}:{password}".encode('utf-8')).decode('utf-8')

        # Додавання закодованої пари у новий список
        encoded_list.append(encoded_pair)

    return encoded_list

# Приклад використання
credentials_list = ['andry:uyro18890D', 'steve:oppjM13LL9e']
result = encode_data_to_base64(credentials_list)
print(result)
