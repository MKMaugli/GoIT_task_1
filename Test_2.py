grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}

def formatted_grades(students):
    formatted_list = []

    # Заголовок таблиці
    header = "| {:<4} | {:<10} | {:^5} | {:^5} |".format("ID", "Name", "Grade", "Points")
    formatted_list.append("-" * len(header))
    formatted_list.append(header)
    formatted_list.append("-" * len(header))

    # Форматування даних для кожного студента
    for idx, (name, grade) in enumerate(students.items(), start=1):
        points = grades.get(grade, 0)
        row = "| {:>4} | {:<10} | {:^5} | {:^5} |".format(idx, name, grade, points)
        formatted_list.append(row)

    formatted_list.append("-" * len(header))
    return formatted_list

# Приклад використання
students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}

for el in formatted_grades(students):
    print(el)
