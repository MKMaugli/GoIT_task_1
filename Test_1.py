from random import randint

def get_random_password():
    password_length = 8
    password = ""

    for _ in range(password_length):
        random_num = randint(40, 126)
        password += chr(random_num)

    return password

# Приклад використання:
generated_password = get_random_password()
print(f"Згенерований пароль: {generated_password}")
