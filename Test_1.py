def amount_payment(payments):
    total_payment = 0
    for payment in payments:
        if payment > 0:
            total_payment += payment
    return total_payment

# Приклад використання:
payments_list = [100, -50, 30, -20, 10]
result = amount_payment(payments_list)
print(f"Сума платежів наприкінці місяця: {result}")
