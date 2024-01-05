import shutil

def unpack(archive_path, path_to_unpack):
    try:
        # Розпакування архіву за допомогою shutil.unpack_archive
        shutil.unpack_archive(archive_path, path_to_unpack)
        print(f"Archive successfully unpacked to: {path_to_unpack}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Приклад використання
archive_path = "шлях_до_архіву/backup_folder.zip"
path_to_unpack = "шлях_до_розпакованої_теки"
unpack(archive_path, path_to_unpack)
