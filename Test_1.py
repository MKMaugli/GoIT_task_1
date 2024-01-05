def save_credentials_users(path, users_info):
    try:
        # Відкриття файлу у бінарному режимі для запису
        with open(path, 'wb') as file:
            # Ітерація по кожному користувачеві в словнику
            for username, password in users_info.items():
                # Створення рядка у вигляді username:password та конвертація його в байти
                user_credentials = f"{username}:{password}\n".encode('utf-8')
                # Запис у файл
                file.write(user_credentials)

    except Exception as e:
        print(f"An error occurred: {e}")

# Приклад використання
users_data = {'andry': 'uyro18890D', 'steve': 'oppjM13LL9e'}
file_path = "шлях_до_вихідного_файлу.bin"
save_credentials_users(file_path, users_data)
