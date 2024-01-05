def add_employee_to_file(record, path):
    # Відкриття файлу за вказаним шляхом у режимі 'a' (для додавання)
    file = open(path, 'a')

    # Додавання співробітника (record) у файл та початок нового рядка
    file.write(record + "\n")

    # Закриття файлу
    file.close()

# Приклад використання
employee_record = "Drake Mikelsson,19"
file_path = "шлях_до_файлу.txt"
add_employee_to_file(employee_record, file_path)
