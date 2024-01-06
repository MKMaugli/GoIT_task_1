def get_employees_by_profession(path, profession):
    try:
        # Відкриваємо файл для читання
        with open(path, 'r') as file:
            # Зчитуємо рядки з файлу
            lines = file.readlines()

            # Знаходимо усі рядки, де є вказана profession
            matching_lines = [line.strip().split(' ', 1)[0] for line in lines if profession in line]

            # Об'єднуємо всі імена в один рядок
            result_str = ' '.join(matching_lines)

        return result_str

    except Exception as e:
        print(f"Error: {e}")
        return None

# Приклад використання:
path = "employees.txt"
profession = "cook"

result = get_employees_by_profession(path, profession)
print(result)
