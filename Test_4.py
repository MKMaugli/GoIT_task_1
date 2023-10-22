result = None
operand = None
operator = None
wait_for_number = True

while True:
    if wait_for_number:
        user_input = input("Enter the number: ")
        try:
            operand = float(user_input)
            if result is None:
                result = operand
            wait_for_number = False
        except ValueError:
            print(f"'{user_input}' is not a valid number. Try again.")
    else:
        user_input = input("Enter the operator (+, -, *, /): ")
        if user_input in ('+', '-', '*', '/'):
            if operator == '+':
                result = result + operand if result is not None else operand
            elif operator == '-':
                result = result - operand if result is not None else operand
            elif operator == '*':
                result = result * operand if result is not None else operand
            elif operator == '/':
                if operand == 0:
                    print("Division by zero is not allowed. Try again.")
                    continue
                result = result / operand if result is not None else operand

            operator = user_input
            wait_for_number = True
        elif user_input == '=':
            if operator is None:
                print("No operator provided. Try again.")
            else:
                if operator == '+':
                    result = result + operand if result is not None else operand
                elif operator == '-':
                    result = result - operand if result is not None else operand
                elif operator == '*':
                    result = result * operand if result is not None else operand
                elif operator == '/':
                    if operand == 0:
                        print("Division by zero is not allowed. Try again.")
                        continue
                    result = result / operand if result is not None else operand
                else:
                    print(f"'{operator}' is not a valid operator. Try again.")
            print(f"Result: {result}")
            break
        else:
            print(f"'{user_input}' is not '+', '-', '*', '/', or '='. Try again.")
