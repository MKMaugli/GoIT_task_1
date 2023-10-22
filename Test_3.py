result = None
operand = None
operator = None

while True:
    try:
        num = input("Введите число (или '=' для вычисления): ")
        if num == '=':
            if result is not None:
                print(f"Результат: {result}")
            else:
                print("Не введено чисел или операторов.")
            break
        operand = float(num)
    except ValueError:
        print("Введено не число. Попробуйте снова.")
        continue

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
                print(f"Результат: {result}")
            break
        else:
            result = operand
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
            
    else:
        print(f"'{operator}' не является допустимым оператором. Попробуйте снова.")
