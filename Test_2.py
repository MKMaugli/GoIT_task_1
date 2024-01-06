def get_employees_by_profession(path, profession):
    with open(path, "r") as f:
        lines = f.readlines()

    found_employees = []
    for line in lines:
        if profession in line:
            found_employees.append(line.split()[0])

    result = " ".join(found_employees)
    return result


# Приклад використання:
path = "employees.txt"
profession = "cook"

result = get_employees_by_profession(path, profession)

print(result)
