def sanitize_phone_number(phone):
    # Удаление всех символов, кроме цифр
    digits_only = ''.join(char for char in phone if char.isdigit())

    # Проверка и преобразование в правильный формат
    if len(digits_only) >= 10:  # если номер содержит 10 или более цифр
        return digits_only
    else:
        return None  # возвращаем None для обозначения некорректного номера

# Пример использования
phone_numbers = [
    "+38(050)123-32-34",
    "0503451234",
]

for phone in phone_numbers:
    sanitized_number = sanitize_phone_number(phone.strip())  # теперь используем strip()
    if sanitized_number:
        print(sanitized_number)
    else:
        print(f"Некорректный номер: {phone}")
