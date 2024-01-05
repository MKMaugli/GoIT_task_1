def get_grade(ects_key):
    ects_grades = {
        "F": 1,
        "FX": 2,
        "E": 3,
        "D": 3,
        "C": 4,
        "B": 5,
        "A": 5
    }

    return ects_grades.get(ects_key, None)

def get_description(ects_key):
    ects_descriptions = {
        "F": "Unsatisfactorily",
        "FX": "Unsatisfactorily",
        "E": "Enough",
        "D": "Satisfactorily",
        "C": "Good",
        "B": "Very good",
        "A": "Perfectly"
    }

    return ects_descriptions.get(ects_key, None)

# Приклад використання:
ects_grade = "D"
grade_value = get_grade(ects_grade)
grade_description = get_description(ects_grade)

if grade_value is not None and grade_description is not None:
    print(f"Оцінка: {grade_value} ({ects_grade}), Пояснення: {grade_description}")
else:
    print("Неправильний ключ ECTS.")
