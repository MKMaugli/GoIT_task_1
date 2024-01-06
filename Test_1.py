def solve_riddle(riddle, word_length, start_letter, reverse=False):
    found_word = ""

    if not isinstance(riddle, str):
        raise TypeError("riddle must be a string")
    if not isinstance(word_length, int) or word_length <= 0:
        raise ValueError("word_length must be a positive integer")
    if not isinstance(start_letter, str):
        raise TypeError("start_letter must be a string")

    if reverse:
        for i in range(len(riddle) - 1, -1, -1):
            if riddle[i] == start_letter:
                # Знаходимо можливий початок слова
                start_pos = i - (word_length - 1)
                if start_pos >= 0:
                    found_word = riddle[start_pos:i + 1][::-1]  # Звертаємо рядок
                    break
    else:
        for i in range(len(riddle)):
            if riddle[i] == start_letter:
                # Знаходимо можливий кінець слова
                end_pos = i + (word_length - 1)
                if end_pos < len(riddle):
                    found_word = riddle[i:end_pos + 1]
                    break

    return found_word

# Приклад використання:
riddle_str = "mi1powperet4"
word_length = 3
start_letter = "r"
reverse = True

result = solve_riddle(riddle_str, word_length, start_letter, reverse)
print(result)
