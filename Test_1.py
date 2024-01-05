def save_applicant_data(source, output):
    try:
        # Відкриття файлу output за допомогою менеджера контексту with у режимі "w"
        with open(output, 'w') as output_file:
            # Ітерація по кожному абітурієнту у списку source
            for applicant in source:
                # Запис прізвища, коду спеціальності та балів у файл через кому
                output_line = f"{applicant['name']},{applicant['specialty']},{applicant['math']},{applicant['lang']},{applicant['eng']}\n"
                # Запис у файл
                output_file.write(output_line)

    except Exception as e:
        print(f"An error occurred: {e}")

# Приклад використання
applicants_data = [
    {
        "name": "Kovalchuk Oleksiy",
        "specialty": 301,
        "math": 175,
        "lang": 180,
        "eng": 155,
    },
    {
        "name": "Ivanchuk Boryslav",
        "specialty": 101,
        "math": 135,
        "lang": 150,
        "eng": 165,
    },
    {
        "name": "Karpenko Dmitro",
        "specialty": 201,
        "math": 155,
        "lang": 175,
        "eng": 185,
    },
]

output_file_path = "шлях_до_вихідного_файлу.txt"
save_applicant_data(applicants_data, output_file_path)
