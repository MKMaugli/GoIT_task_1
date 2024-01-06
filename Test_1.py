from datetime import datetime

def get_str_date(date):
    # Перетворюємо рядок у форматі ISO в об'єкт datetime
    datetime_obj = datetime.fromisoformat(date.replace('Z', '+00:00'))

    # Отримуємо назву дня тижня
    day_of_week = datetime_obj.strftime('%A')

    # Отримуємо число, місяць та рік
    day = datetime_obj.day
    month = datetime_obj.strftime('%B')
    year = datetime_obj.year

    # Додаємо "0" спереду для чисел від 1 до 9
    formatted_day = f'{day:02}'

    # Повертаємо перетворену дату у вказаному форматі
    return f'{day_of_week} {formatted_day} {month} {year}'

# Приклад використання:
input_date = '2021-03-03 17:12:40.478Z'
result = get_str_date(input_date)
print(result)
