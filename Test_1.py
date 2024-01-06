def sequence_buttons(string):
    # Словник символів для кнопок
    button_mapping = {
        '1': '.,?!:',
        '2': 'ABC',
        '3': 'DEF',
        '4': 'GHI',
        '5': 'JKL',
        '6': 'MNO',
        '7': 'PQRS',
        '8': 'TUV',
        '9': 'WXYZ',
        '0': ' '
    }

    # Початковий рядок для послідовності кнопок
    result_sequence = ""

    # Перетворення тексту
    for char in string:
        char_upper = char.upper()
        for button, symbols in button_mapping.items():
            if char_upper in symbols:
                button_presses = symbols.index(char_upper) + 1
                result_sequence += str(button) * button_presses

    return result_sequence

# Приклад використання:
input_text = "Hi there!"
result_sequence = sequence_buttons(input_text)
print(result_sequence)
