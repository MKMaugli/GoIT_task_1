import os
import shutil
import zipfile
import gzip
import tarfile
import rarfile
import bz2
import lzma

SOURCE_PATH = r'C:\Users\mitya\Desktop\Spam\goit'
DESTINATION_FOLDER = r'C:\Users\mitya\Desktop\Spam\GoIT_6HM'

CATEGORIES = {
  "images": ("jpeg", "png", "jpg", "svg", "ico", "gif", "tiff", "webp"),
  "video": ("avi", "mp4", "mov", "mkv", "wmv", "webm"),
  "documents": ("doc", "docx", "txt", "pdf", "xlsx", "pptx", "csv", "odp", "ods", "ppt", "xls", "odt", "rtf"),
  "audio": ("mp3", "ogg", "wav", "amr", "flac"),
  "other": ()
}

ARCHIVES = ["zip", "gz", "tar", "rar", "7z"]

def normalize(name):
  """
  Нормалізує ім'я файлу, видаляючи пробіли та інші непотрібні символи.

  Приймає на вхід ім'я файлу.
  """

  new_name = name.replace(" ", "_")
  return new_name

def process_folder(path, destination_path):
  """
  Обробляє папку та всі її вкладення.

  Приймає на вхід шлях до папки та шлях до папки призначення.
  """
  # Створюємо папки, якщо їх немає
  for category in ["images", "video", "documents", "other"]:
    destination_folder = os.path.join(destination_path, category)
    if not os.path.exists(destination_folder):
      os.mkdir(destination_folder)

  # Отримуємо розширення файлу
  for file in os.listdir(path):
    file_path = os.path.join(path, file)
    if os.path.isdir(file_path):
      # Рекурсивно обробляємо вкладені папки
      process_folder(file_path, destination_path)
    else:
      # Переконвертуємо назву файлу
      new_name = normalize(file)
      new_folder = category
      extension = file.split(".")[-1]
      if extension in ARCHIVES:
        new_folder = "archives"
        category = "archives"
        shutil.move(file_path, os.path.join(destination_path, new_folder, new_name))
        if extension == "7z":
          with lzma.open(os.path.join(destination_path, "archives", file), "rb") as file_stream:
            with rarfile.RarFile(file_stream) as rar_archive:
              rar_archive.extractall(destination_path)
            os.remove(os.path.join(destination_path, file))
        else:
          new_folder = "archives"

      if os.path.exists(os.path.join(destination_path, file)):
        shutil.move(file_path, os.path.join(destination_path, new_folder, new_name))

      # Для 7z архівів потрібно використовувати модулі lzma і rarfile
      with rarfile.RarFile(os.path.join(destination_path, file)) as archive:
        archive.extractall(destination_path)
        os.remove(os.path.join(destination_path, file))

      # Файл з невідомим розширенням
      if extension not in ARCHIVES:
        # Переміщуємо файл у папку other
        destination_folder = os.path.join(destination_path, "other")
        shutil.move(os.path.join(path, new_name), destination_folder)


if __name__ == "__main__":
  # Вказуємо папку, з якої потрібно перенести файли
  source_path = SOURCE_PATH

  # Вказуємо шлях до папки, в яку потрібно перенести файли
  destination_path = DESTINATION_FOLDER

  # Проходимося по папці source_path та переносимо файли в destination_path
  process_folder(source_path, destination_path)
