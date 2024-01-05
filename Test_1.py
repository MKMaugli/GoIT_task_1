def formatted_numbers():
    result = []

    header = "| decimal  |   hex    |  binary  |"
    format_str = "|{:<10}|{:^10}|{:>10}|"

    result.append(header)

    for num in range(16):
        decimal = num
        hex_num = hex(num)[2:]
        binary = bin(num)[2:]
        formatted_line = format_str.format(decimal, hex_num, binary)
        result.append(formatted_line)

    return result

# Виведемо результат
for el in formatted_numbers():
    print(el)
