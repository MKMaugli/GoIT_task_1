def format_string(string, length):
    string_characters = len(string)
    
    if string_characters >= length:
        # print(string)
        return(string)
    else:
        spaces_to_add = max(0, (length - len(string)) // 2)
        padded_string = " " * spaces_to_add + string
        # print(padded_string)
        return(padded_string)


format_string (length=15, string='abaa')

# # Введення рядка
# user_input = input("Введіть рядок: ")
# length = 15

# # Обчислення кількості символів у рядку
# num_characters = len(user_input)

# # Розрахунок кількості пробілів, які треба додати перед рядком
# spaces_to_add = max(0, (length - len(user_input)) // 2)

# # Додавання пробілів перед рядком
# padded_string = " " * spaces_to_add + user_input

# # Виведення результату
# print(f"Кількість символів у введеному рядку: {num_characters}")
# print(f"Рядок з доданими пробілами: {padded_string}")

# spaces_to_add = max(0, (num_characters - len(length)) // 2)

#get_fullname ("Petro", "Zaliznyak")