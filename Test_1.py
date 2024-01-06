from datetime import datetime

def get_days_from_today(date):
    # Перетворюємо рядок з датою в об'єкт datetime
    target_date = datetime.strptime(date, "%Y-%m-%d")
    
    # Отримуємо поточну дату
    current_date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    
    # Визначаємо різницю у днях і повертаємо її
    days_difference = (current_date - target_date).days
    return days_difference

# Приклад використання:
current_date = datetime.now().strftime("%Y-%m-%d")
result = get_days_from_today("1989-08-15")
print(f"Кількість днів з {current_date} до 1989-08-15: {result}")
