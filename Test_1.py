grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}

def formatted_grades(students):
    result = []

    for i, (name, grade) in enumerate(students.items(), start=1):
        points = grades.get(grade, 0)
        formatted_line = "{:>4}|{:<10}|{:^5}|{:^5}".format(i, name, grade, points)
        result.append(formatted_line)

    return result

# Приклад використання
students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}

for el in formatted_grades(students):
    print(el)
