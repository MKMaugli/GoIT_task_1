def sanitize_file(source, output):
    try:
        # Відкриття файлу source за допомогою менеджера контексту with у режимі "r"
        with open(source, 'r') as source_file:
            # Читання вмісту файла та очищення від цифр
            source_content = ''.join(char for char in source_file.read() if not char.isdigit())

        # Відкриття файлу output за допомогою менеджера контексту with у режимі "w"
        with open(output, 'w') as output_file:
            # Запис очищеного вмісту файла у файл output
            output_file.write(source_content)

    except Exception as e:
        print(f"An error occurred: {e}")

# Приклад використання
source_file_path = "шлях_до_вихідного_файлу.txt"
output_file_path = "шлях_до_очищеного_файлу.txt"
sanitize_file(source_file_path, output_file_path)
