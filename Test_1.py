from random import randint


def get_random_password():
    result = ""
    count = 0
    while count < 8:
        random_symbol = chr(randint(40, 126))
        result = result + random_symbol
        count = count + 1
    return result


def is_valid_password(password):
    if len(password) != 8:
        return False

    has_upper = False
    has_lower = False
    has_num = False

    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_num = True

    return has_upper and has_lower and has_num

def get_password():
    max_attempts = 100
    current_attempt = 0

    while current_attempt < max_attempts:
        password_candidate = get_random_password()

        if is_valid_password(password_candidate):
            return password_candidate

        current_attempt += 1

    # Якщо не вдається згенерувати надійний пароль за обмежену кількість спроб,
    # можна повернути None або викинути виняток, залежно від вашого бажання.
    return None

# Приклад використання:
generated_password = get_password()

if generated_password:
    print(f"Згенерований надійний пароль: {generated_password}")
else:
    print("Не вдалося згенерувати надійний пароль за обмежену кількість спроб.")
