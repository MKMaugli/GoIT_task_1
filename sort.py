import os
import shutil
import string

#folder_path = "C:\\Users\\mitya\\Desktop\\Spam\\goit"
folder_path = r'C:\Users\mitya\Desktop\Spam\goit'
destination_folder = r'C:\Users\mitya\Desktop\Spam\GoIT_6HM'


# Функція для транслітерації та нормалізації імен файлів
def normalize(name):
    transliteration = str.maketrans("абвгдеёжзийклмнопрстуфхцчшщъыьэюя",
                                     "a|b|v|g|d|e|yo|zh|z|i|y|k|l|m|n|o|p|r|s|t|u|f|h|ts|ch|sh|shch|'|y|'|e|yu|ya")

    name = name.translate(transliteration)
    name = ''.join(c if c.isalnum() or c in {'_', '.'} else '_' for c in name)
    return name

# Функція для обробки папок та сортування файлів
def process_folder(folder_path, destination_folder):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            extension = file.split('.')[-1].upper()

            new_name = normalize(file)
            new_path = os.path.join(root, new_name)

            # Перейменовуємо файл
            os.rename(file_path, new_path)

            # Розбиваємо на категорії та переміщаємо файли
            if extension in {'JPEG', 'PNG', 'JPG', 'SVG'}:
                shutil.move(new_path, os.path.join(destination_folder, 'images', new_name))
            elif extension in {'AVI', 'MP4', 'MOV', 'MKV'}:
                shutil.move(new_path, os.path.join(destination_folder, 'video', new_name))
            elif extension in {'DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX'}:
                shutil.move(new_path, os.path.join(destination_folder, 'documents', new_name))
            elif extension in {'MP3', 'OGG', 'WAV', 'AMR'}:
                shutil.move(new_path, os.path.join(destination_folder, 'audio', new_name))
            elif extension in {'ZIP', 'GZ', 'TAR'}:
                archive_folder = os.path.join(destination_folder, 'archives', new_name.split('.')[0])
                os.makedirs(archive_folder, exist_ok=True)
                shutil.unpack_archive(new_path, archive_folder)
                os.remove(new_path)
            else:
                shutil.move(new_path, os.path.join(destination_folder, 'other', new_name))

    # Видаляємо порожні папки
    for root, dirs, files in os.walk(folder_path, topdown=False):
        for folder in dirs:
            folder_path = os.path.join(root, folder)
            if not os.listdir(folder_path):
                os.rmdir(folder_path)

# Основна функція для обробки аргументів командного рядка
def main():
    import sys

    if len(sys.argv) != 3:
        print("Usage: python script.py /path/to/folder /destination/folder")
        sys.exit(1)

    # folder_path = sys.argv[1]
    # destination_folder = sys.argv[2]
    
    # Перевірка існування та доступності папок
    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' not found.")
        sys.exit(1)
    if not os.path.exists(destination_folder):
        print(f"Error: Destination folder '{destination_folder}' not found.")
        sys.exit(1)

    # Визначаємо шляхи для категорій у папці призначення
    for category in ['images', 'video', 'documents', 'audio', 'archives', 'other']:
        os.makedirs(os.path.join(destination_folder, category), exist_ok=True)

    process_folder(folder_path, destination_folder)
    
    # Збираємо інформацію про файли в кожній категорії
    image_files = os.listdir(os.path.join(folder_path, 'images'))
    video_files = os.listdir(os.path.join(folder_path, 'video'))
    document_files = os.listdir(os.path.join(folder_path, 'documents'))
    audio_files = os.listdir(os.path.join(folder_path, 'audio'))
    archive_files = os.listdir(os.path.join(folder_path, 'archives'))
    other_files = os.listdir(os.path.join(folder_path, 'other'))

    # Виводимо інформацію про файли в кожній категорії
    print_category_info('Images', image_files)
    print_category_info('Video', video_files)
    print_category_info('Documents', document_files)
    print_category_info('Audio', audio_files)
    print_category_info('Archives', archive_files)
    print_category_info('Other', other_files)

    # Збираємо розширення файлів
    extensions = {file.split('.')[-1].upper() for file in os.listdir(folder_path)}

    # Знаходимо невідомі розширення
    known_extensions = {'JPEG', 'PNG', 'JPG', 'SVG', 'AVI', 'MP4', 'MOV', 'MKV',
                        'DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX', 'MP3', 'OGG', 'WAV', 'AMR',
                        'ZIP', 'GZ', 'TAR'}
    unknown_extensions = extensions - known_extensions

    # Виводимо розширення
    print("\nKnown Extensions:")
    for ext in known_extensions:
        print(f"- {ext}")

    print("\nUnknown Extensions:")
    for ext in unknown_extensions:
        print(f"- {ext}")

def print_category_info(category, files):
    print(f"Category: {category}")
    print("Files:")
    for file in files:
        print(f"- {file}")
    print()

if __name__ == "__main__":
    main()
