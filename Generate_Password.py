from random import randint
p_len = input('Inpup passwort lenght: ')
# print (p_len)

def get_random_password():
    password_length = int(p_len)
    password = ""

    for _ in range(password_length):
        random_num = randint(40, 126)
        password += chr(random_num)

    return password

def is_valid_password(password):
    # Критерії надійного пароля:
    uppercase_criteria = any(char.isupper() for char in password)
    lowercase_criteria = any(char.islower() for char in password)
    digit_criteria = any(char.isdigit() for char in password)

    # Перевірка на відповідність всіх критеріїв
    return uppercase_criteria and lowercase_criteria and digit_criteria

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

# # Приклад використання:
# generated_password = get_random_password()
# print(f"Згенерований пароль: {generated_password}")

# password_to_check = generated_password
# result = is_valid_password(password_to_check)

# if result:
#     print("Пароль відповідає критеріям надійності.")
# else:
#     print("Пароль не відповідає критеріям надійності.")
    
# Приклад використання:
generated_password = get_password()

if generated_password:
    print(f"Згенерований надійний пароль: {generated_password}")
else:
    print("Не вдалося згенерувати надійний пароль за обмежену кількість спроб.")

