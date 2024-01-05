def total_salary(path):
    total = 0.0

    # Відкриття файлу за вказаним шляхом
    file = open(path, 'r')

    # Читання рядка за рядком
    line = file.readline()
    while line:
        # Розбиття рядка на ім'я та зарплату за допомогою коми
        name, salary_str = line.strip().split(',')

        # Перетворення зарплати в число та додавання до загальної суми
        total += float(salary_str)

        # Читання наступного рядка
        line = file.readline()

    # Закриття файлу
    file.close()

    # Повернення загальної суми у вигляді float
    return total

# Приклад використання
file_path = "шлях_до_файлу.txt"
total_salary_value = total_salary(file_path)
print(f"Загальна заробітна плата: {total_salary_value}")
