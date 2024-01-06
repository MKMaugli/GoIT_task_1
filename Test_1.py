def to_indexed(path, output_path):
    try:
        # Відкриваємо вхідний файл для читання
        with open(path, 'r') as source:
            # Відкриваємо вихідний файл для запису
            with open(output_path, 'w') as output:
                # Зчитуємо всі рядки з вхідного файлу
                lines = source.readlines()

                # Записуємо змінений вміст у вихідний файл
                for i, line in enumerate(lines):
                    output.write(f"{i}: {line}")

        print("Операція успішно виконана.")

    except Exception as e:
        print(f"Помилка: {e}")



# Приклад використання:
source_file = "input.txt"
output_file = "output.txt"
to_indexed(source_file, output_file)
