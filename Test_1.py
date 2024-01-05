def is_valid_password(password):
    # Критерії надійного пароля:
    length_criteria = len(password) == 8
    uppercase_criteria = any(char.isupper() for char in password)
    lowercase_criteria = any(char.islower() for char in password)
    digit_criteria = any(char.isdigit() for char in password)

    # Перевірка на відповідність всіх критеріїв
    return length_criteria and uppercase_criteria and lowercase_criteria and digit_criteria

# Приклад використання:
password_to_check = "Abcd1234"
result = is_valid_password(password_to_check)

if result:
    print("Пароль відповідає критеріям надійності.")
else:
    print("Пароль не відповідає критеріям надійності.")
