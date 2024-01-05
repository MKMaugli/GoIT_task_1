from pathlib import Path

def parse_folder(path):
    files = []
    folders = []
    
    directory_path = Path(path)

    if not directory_path.is_dir():
        print(f"Шлях {path} не вказує на теку або такий шлях не існує.")
        return files, folders

    for item in directory_path.iterdir():
        if item.is_file():
            files.append(item)
        elif item.is_dir():
            folders.append(item)

    return files, folders

# Приклад використання:
folder_to_parse = '/path/to/parse'  # Замініть на шлях, де ви хочете аналізувати теку

result_files, result_folders = parse_folder(folder_to_parse)

if result_files:
    print("Знайдені файли:")
    for file_path in result_files:
        print(file_path)

if result_folders:
    print("Знайдені теки:")
    for folder_path in result_folders:
        print(folder_path)

if not result_files and not result_folders:
    print(f"В {folder_to_parse} не знайдено файли або теки.")
