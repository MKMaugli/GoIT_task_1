def write_employees_to_file(employee_list, path):
    # Відкриття файлу за вказаним шляхом у режимі "w"
    file = open(path, 'w')

    # Проходження по кожному відділу та кожному співробітнику
    for department_employees in employee_list:
        for employee_info in department_employees:
            # Запис рядка співробітника у файл та додавання нового рядка
            file.write(f"{employee_info}\n")

    # Закриття файлу
    file.close()

# Приклад використання
employees_data = [['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']]
file_path = "шлях_до_файлу.txt"
write_employees_to_file(employees_data, file_path)
