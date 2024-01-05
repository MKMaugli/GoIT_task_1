import shutil

def create_backup(path, file_name, employee_residence):
    try:
        # Збереження даних словника у бінарний файл
        with open(f"{path}/{file_name}", 'wb') as file:
            for name, country in employee_residence.items():
                # Запис пари ім'я-країна у бінарний файл
                line = f"{name} {country}\n"
                file.write(line.encode('utf-8'))

        # Створення архіву
        shutil.make_archive(f"backup_{path}", 'zip', path)

        # Повернення шляху до створеного архіву
        return f"{path}/backup_folder.zip"

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Приклад використання
employee_residence_data = {'Michael': 'Canada', 'John': 'USA', 'Liza': 'Australia'}
backup_path = "шлях_до_теки"
backup_file_name = "backup_data.bin"
result = create_backup(backup_path, backup_file_name, employee_residence_data)

if result:
    print(f"Backup created successfully at: {result}")
