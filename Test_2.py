result = None
operand = None
operator = None

while True:
    try:
        operand = float(input("Введите число: "))
    except ValueError:
        print("Введено не число. Попробуйте снова.")
        continue

    while True:
        operator = input("Введите оператор (+, -, *, /) или '=' для вычисления: ")

        if operator == '=':
            if result is not None:
                if operator != '=':
                    if operator == '+':
                        result = result + operand
                    elif operator == '-':
                        result = result - operand
                    elif operator == '*':
                        result = result * operand
                    elif operator == '/':
                        if operand != 0:
                            result = result / operand
                        else:
                            print("Деление на ноль невозможно.")
                    else:
                        print(f"Результат: {result}")
                else:
                    result = operand
                print(f"Результат: {result}")
                break
            else:
                result = operand
                break
        elif operator in "+-*/":
            if result is not None:
                if operator == '+':
                    result = result + operand
                elif operator == '-':
                    result = result - operand
                elif operator == '*':
                    result = result * operand
                elif operator == '/':
                    if operand != 0:
                        result = result / operand
                    else:
                        print("Деление на ноль невозможно.")
                        break
            else:
                result = operand
            break
        else:
            print(f"'{operator}' не является допустимым оператором. Попробуйте снова.")
