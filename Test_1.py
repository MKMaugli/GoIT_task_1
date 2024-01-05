def read_employees_from_file(path):
    # Відкриття файлу за вказаним шляхом у режимі "r"
    file = open(path, 'r')

    # Ініціалізація списку співробітників
    employees_list = []

    # Читання кожного рядка з файлу
    line = file.readline()
    while line:
        # Додавання рядка без символу кінця рядка до списку
        employees_list.append(line.strip())

        # Читання наступного рядка
        line = file.readline()

    # Закриття файлу
    file.close()

    # Повернення списку співробітників
    return employees_list

# Приклад використання
file_path = "шлях_до_файлу.txt"
employees_data = read_employees_from_file(file_path)
print(employees_data)
