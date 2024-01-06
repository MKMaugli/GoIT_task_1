from datetime import date

def get_days_in_month(month, year):
    # Перевіряємо чи місяць коректний
    if month < 1 or month > 12:
        raise ValueError("Некоректний номер місяця. Введіть число від 1 до 12.")

    # Визначаємо кількість днів у місяці
    if month in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    elif month in {4, 6, 9, 11}:
        return 30
    else:
        # Перевіряємо чи рік високосний
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            return 29  # Високосний рік
        else:
            return 28  # Звичайний рік

# Приклад використання:
month = 2
year = 2024
result = get_days_in_month(month, year)
print(f"У {month}-му місяці {year} року {result} днів.")
