def file_operations(path, additional_info, start_pos, count_chars):
    try:
        # Відкриваємо файл для додавання інформації
        with open(path, 'a') as file:
            # Додаємо додаткову інформацію
            file.write(additional_info)

        # Відкриваємо той самий файл для читання
        with open(path, 'r') as file:
            # Переміщуємо курсор на позицію start_pos
            file.seek(start_pos)
            
            # Зчитуємо рядок довжиною count_chars
            result_str = file.read(count_chars)

        return result_str

    except Exception as e:
        print(f"Error: {e}")
        return None

# Приклад використання:
path = "example.txt"
additional_info = "Additional Information"
start_pos = 5
count_chars = 10

result = file_operations(path, additional_info, start_pos, count_chars)
print(result)
