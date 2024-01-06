def solve_riddle(riddle, word_length, start_letter, reverse=False):
    found_word = None

    if not isinstance(riddle, str):
        raise TypeError("riddle must be a string")
    if not isinstance(word_length, int) or word_length <= 0:
        raise ValueError("word_length must be a positive integer")
    if not isinstance(start_letter, str):
        raise TypeError("start_letter must be a string")

    if reverse:
        for i in range(len(riddle) - 1, -word_length - 1, -1):
            if riddle[i] == start_letter:
                found_word = riddle[i:i + word_length]
                break
    else:
        for i in range(len(riddle)):
            if riddle[i] == start_letter:
                found_word = riddle[i:i + word_length]
                break
    return found_word

# Приклад використання:
riddle_str = "mi1powperet4"
word_length = 3
start_letter = "r"
reverse = True

result = solve_riddle(riddle_str, word_length, start_letter, reverse)
print(result)