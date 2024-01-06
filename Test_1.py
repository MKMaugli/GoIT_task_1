import re

def token_parser(s):
    # Визначимо шаблон для пошуку чисел, операторів і дужок
    pattern = r'\d+|\+|-|\*|/|\(|\)'  # \d+ - послідовність цифр, оператори, дужки
    
    # Використаємо findall для знаходження всіх лексем у рядку
    tokens = re.findall(pattern, s)

    # Видалимо можливі прогалини з лексем
    tokens = [token.strip() for token in tokens if token.strip()]

    return tokens

# Приклад використання:
expression = "2+ 34-5 * 3"
result = token_parser(expression)
print(result)
