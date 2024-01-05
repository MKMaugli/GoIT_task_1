def is_valid_pin_codes(pin_codes):
    # Перевірка на порожній список.
    if not pin_codes:
        return False

    # Перевірка на наявність дублікатів та правильний формат.
    unique_pins = set(pin_codes)
    if len(unique_pins) != len(pin_codes):
        return False

    for pin in unique_pins:
        if len(pin) != 4 or not pin.isdigit():
            return False

    return True

# Приклад використання:
pin_codes = ['1101', '9034', '0011']

result = is_valid_pin_codes(pin_codes)
print(result)
