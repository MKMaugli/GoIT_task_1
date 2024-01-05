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

# Приклад використання:
generated_password = get_random_password()
print(f"Згенерований пароль: {generated_password}")
