grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}

def formatted_grades(students):
    formatted_list = []

    for idx, (name, grade) in enumerate(students.items(), start=1):
        points = grades.get(grade, 0)
        row = "{:>2}|{:<8}|{:^4}|{:^4}".format(idx, name, grade, points)
        formatted_list.append(row)

    return formatted_list

# Приклад використання
students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}

for el in formatted_grades(students):
    print(el)
