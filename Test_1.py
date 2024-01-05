from pathlib import Path  # Додаємо імпорт Path

print("Поточна директорія:", Path.cwd())

def parse_folder(path):
    files = []
    folders = []
    
    for item in path.iterdir():
        if item.is_file():
            files.append(item.name)
        elif item.is_dir():
            folders.append(item.name)
            
    return files, folders


# Замість цього
# result_files, result_folders = parse_folder

# Викликаємо функцію без витягування результату в змінні
# parse_folder()

# Викликаємо функцію та отримуємо результат
# result_files, result_folders = parse_folder()

result_files, result_folders = parse_folder(Path('C:\_testData'))

if result_files:
    print("Знайдені файли:")
    for file_path in result_files:
        print(file_path)

if result_folders:
    print("Знайдені теки:")
    for folder_path in result_folders:
        print(folder_path)

if not result_files and not result_folders:
    print(f"В текі не знайдено файлів або тек.")

