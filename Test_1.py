def get_credentials_users(path):
    try:
        # Відкриття файлу у бінарному режимі для читання
        with open(path, 'rb') as file:
            # Читання вмісту файлу та конвертація байтів у рядки
            content = [line.decode('utf-8').strip() for line in file]

        return content

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Приклад використання
file_path = "шлях_до_вхідного_файлу.bin"
result = get_credentials_users(file_path)

if result:
    print(result)
